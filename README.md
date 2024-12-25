<!--
SPDX-FileCopyrightText: 2024 Thomas Breitner

SPDX-License-Identifier: MIT
-->

# mkdocs-quizdown-plugin

**🔥 This is work in progress - no liability for nothing.**

- Allows embedding [quizdown-js](https://github.com/bonartm/quizdown-js) quizzes in MkDocs pages
- Try the [quizdown live editor](https://bonartm.github.io/quizdown-live-editor/) from the author of `quizdown-js` to create your quiz markdown
- MkDocs integration demo: [`docs/index.md`](docs/index.md)

## Install

*Currently only available via it's git repository.*

```bash
# Initial install:
python -m pip install \
  'mkdocs-quizdown-plugin @ git+https://github.com/tombreit/mkdocs-quizdown-plugin'

# Upgrade plugin:
python -m pip install \
  --upgrade --no-deps --force-reinstall \
  'mkdocs-quizdown-plugin @ git+https://github.com/tombreit/mkdocs-quizdown-plugin'
```

## Configuration

See [`mkdocs.yml`](https://github.com/tombreit/mkdocs-quizdown-plugin/blob/main/mkdocs.yml)
