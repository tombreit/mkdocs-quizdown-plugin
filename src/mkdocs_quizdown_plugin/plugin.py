# SPDX-FileCopyrightText: 2024 Thomas Breitner
#
# SPDX-License-Identifier: MIT

"""
A plugin that integrates quizdown-js into MkDocs.

quizdown-js is a JavaScript library for creating quizzes in Markdown
from Malte Bonart https://maltebonart.de: https://github.com/bonartm/quizdown-js
"""

import re
from pathlib import Path

from mkdocs.plugins import BasePlugin
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page
from mkdocs.structure.files import Files
from mkdocs.utils import copy_file


class QuizdownPlugin(BasePlugin):
    """
    A plugin that integrates quizdown-js into MkDocs.
    """

    # Order matters.
    ASSETS = [
        "assets/quizdown.js",
        "assets/quizdown_init.js",
    ]

    def __init__(self):
        self._quiz_blocks = {}

    # I inject th JS file in the post_build event to be only available on pages
    # that have quizdown blocks.
    # def on_config(self, config: MkDocsConfig) -> MkDocsConfig | None:
    #     for asset in ASSETS:
    #         if asset.endswith(".js"):
    #             config["extra_javascript"] = [asset] + config["extra_javascript"]
    #     return config

    def on_post_build(self, *, config: MkDocsConfig) -> None:
        if not self._quiz_blocks:
            return

        current_dir = Path(__file__).parent
        for asset in self.ASSETS:
            src_file_path = current_dir / asset
            dest_file_path = Path(config["site_dir"], asset)
            copy_file(src_file_path, dest_file_path)

    def on_page_markdown(
        self, markdown: str, /, *, page: Page, config: MkDocsConfig, files: Files
    ) -> str | None:
        page_url = page.file.url

        pattern = r":::\{quizdown\}\s*\n(.*?)\n:::"
        matches = list(re.finditer(pattern, markdown, re.DOTALL))

        for index, match in enumerate(matches, start=1):
            block = match.group(1)
            placeholder = f"<!--QUIZDOWN_{index}-->"

            if page_url not in self._quiz_blocks:
                self._quiz_blocks[page_url] = []
            self._quiz_blocks[page_url].append(block)

            markdown = markdown.replace(match.group(0), placeholder, 1)

        return markdown

    def on_page_content(
        self, html: str, /, *, page: Page, config: MkDocsConfig, files: Files
    ) -> str | None:
        if page.file.url in self._quiz_blocks:
            page_quizzes = self._quiz_blocks[page.file.url]

            for index, block_content in enumerate(page_quizzes, start=1):
                placeholder = f"<!--QUIZDOWN_{index}-->"
                block_content = f'<div style="visibility: hidden;" class="quizdown">\n{block_content}\n</div>\n'

                # Check if this is the last iteration
                if index == len(page_quizzes):
                    script_tags = "\n".join(
                        f'<script src="{config["site_url"]}{asset}"></script>'
                        for asset in self.ASSETS
                    )
                    block_content = f"""
                        {block_content}
                        {script_tags}
                    """

                html = html.replace(placeholder, block_content, 1)

        return html
