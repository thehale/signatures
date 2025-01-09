<!--
 Copyright (c) 2025 Joseph Hale
 
 This Source Code Form is subject to the terms of the Mozilla Public
 License, v. 2.0. If a copy of the MPL was not distributed with this
 file, You can obtain one at https://mozilla.org/MPL/2.0/.
-->

# Contributing

## Environment Setup

**Install Poetry**

`signatures` uses Poetry for dependency management and for publishing to PyPI.

```bash
curl -sSL https://install.python-poetry.org | POETRY_VERSION=1.8.5 python3 -
```

OR choose another [installation method from Poetry's website](https://python-poetry.org/docs/#installing-with-the-official-installer).

**Install Dependencies**

```bash
poetry shell
poetry install
```


## Running Tests

```bash
poetry run pytest
```

