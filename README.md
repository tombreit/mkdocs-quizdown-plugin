<!--
SPDX-FileCopyrightText: 2024 Thomas Breitner

SPDX-License-Identifier: MIT
-->

# mkdocs-quizdown-plugin

**🔥 This is work in progress - no liability for nothing.**

- Allows embedding [quizdown-js](https://github.com/bonartm/quizdown-js) quizzes in MkDocs pages
- Multiple quizzes can be embedded on multiple pages, and/or
- Multiple quizzes can be embedded on one page
- `quizdown-js` Javascript library included, no CDNs involved

## Demo

<https://tombreit.github.io/mkdocs-quizdown-plugin/>

## Install

### via PyPI

<https://pypi.org/project/mkdocs-quizdown-plugin/>

### via git

```bash
# Initial install:
python -m pip install \
  'mkdocs-quizdown-plugin @ git+https://github.com/tombreit/mkdocs-quizdown-plugin'

# Upgrade plugin:
python -m pip install \
  --upgrade --no-deps --force-reinstall \
  'mkdocs-quizdown-plugin @ git+https://github.com/tombreit/mkdocs-quizdown-plugin'
```

You can use the requirement item `'mkdocs-quizdown-plugin @ git+https://github.com/tombreit/mkdocs-quizdown-plugin'` in your `requirements.txt`:

```text
# file: requirements.txt

mkdocs
mkdocs-quizdown-plugin @ git+https://github.com/tombreit/mkdocs-quizdown-plugin
```

## Configuration

See [`mkdocs.yml`](https://github.com/tombreit/mkdocs-quizdown-plugin/blob/main/mkdocs.yml)

## Usage
*Currently only available via it's git repository.*

Embed your quiz as a Markdown block in your MkDocs Markdown page and enclose it with the mkdocs-quizdown start (`:::{quizdown}`) and end markers (`:::`):

```md
# Quiz

Some **markdown** content.

:::{quizdown}

---
primaryColor: steelblue
shuffleQuestions: false
shuffleAnswers: true
---

# What is the capital of France?

> Paris is the capital and largest city of France.

1. [x] Paris
2. [ ] London
3. [ ] Berlin
4. [ ] Madrid

:::

Some **markdown** content.
```

- Try the [quizdown live editor](https://bonartm.github.io/quizdown-live-editor/) from the author of `quizdown-js` to prepare your quiz markdown
- [quizdown-js configuration options](https://github.com/bonartm/quizdown-js/blob/main/docs/options.md)
- MkDocs integration demo: [`docs/index.md`](docs/index.md)

## Credits

- [quizdown-js by Malte Bonart](https://github.com/bonartm/quizdown-js)
- [MkDocs](https://www.mkdocs.org/)
