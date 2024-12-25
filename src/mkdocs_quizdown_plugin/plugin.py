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


# Order matters.
ASSETS = [
    "assets/quizdown.js",
    "assets/quizdown_init.js",
]


class QuizdownPlugin(BasePlugin):
    """
    A plugin that integrates quizdown-js into MkDocs.
    """

    def __init__(self):
        self._quiz_blocks = []

    # I inject th JS file in the post_build event to be only available on pages
    # that have quizdown blocks.
    # def on_config(self, config: MkDocsConfig) -> MkDocsConfig | None:
    #     for asset in ASSETS:
    #         if asset.endswith(".js"):
    #             config["extra_javascript"] = [asset] + config["extra_javascript"]

    #     return config

    def on_post_build(self, *, config: MkDocsConfig) -> None:
        current_dir = Path(__file__).parent
        for asset in ASSETS:
            src_file_path = current_dir / asset
            dest_file_path = Path(config["site_dir"], asset)
            copy_file(src_file_path, dest_file_path)

    def on_page_markdown(
        self, markdown: str, /, *, page: Page, config: MkDocsConfig, files: Files
    ) -> str | None:
        pattern = r":::\{quizdown\}\s*\n(.*?)\n:::"
        matches = list(re.finditer(pattern, markdown, re.DOTALL))

        for index, match in enumerate(matches, start=1):
            block = match.group(1)
            placeholder = f"<!--QUIZDOWN_{index}-->"
            self._quiz_blocks.append(block)
            markdown = markdown.replace(match.group(0), placeholder, 1)

        return markdown

    def on_page_content(
        self, html: str, /, *, page: Page, config: MkDocsConfig, files: Files
    ) -> str | None:
        quiz_blocks_total = len(self._quiz_blocks)
        for index, block_content in enumerate(self._quiz_blocks, start=1):
            placeholder = f"<!--QUIZDOWN_{index}-->"
            block_content = f'<div style="visibility: hidden;" class="quizdown">\n{block_content}\n</div>\n'

            # Check if this is the last iteration
            if index == quiz_blocks_total:
                script_tags = "\n".join(
                    f'<script src="{config["site_url"]}{asset}"></script>'
                    for asset in ASSETS
                )
                block_content = f"""
                    {block_content}
                    {script_tags}
                """

            html = html.replace(placeholder, block_content, 1)

        return html
