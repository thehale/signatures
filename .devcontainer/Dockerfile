# Copyright (c) 2022 Joseph Hale
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

FROM thehale/python-poetry:1.3.1-py3.8-slim
ARG PROJECT_FOLDER_NAME
ENV PROJECT_ROOT_DIR=/workspaces/$PROJECT_FOLDER_NAME

RUN apt update \
    && apt install git make --assume-yes --no-install-recommends

WORKDIR $PROJECT_ROOT_DIR
ENV PATH="$PROJECT_ROOT_DIR/.venv/bin:$PATH"
