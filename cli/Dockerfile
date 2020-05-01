FROM python:3.8-alpine3.10

WORKDIR /app

ARG POETRY="https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py"
ARG BUILD_DEPS="curl gcc libc-dev make"

# Copy using poetry.lock* in case it doesn't exist yet
COPY ./pyproject.toml ./poetry.lock* /app/

# Install packages
RUN apk add --no-cache --virtual .build-deps $BUILD_DEPS \
    && curl -sSL $POETRY | POETRY_HOME=/opt/poetry python \
    && cd /usr/local/bin \
    && ln -s /opt/poetry/bin/poetry \
    && poetry config virtualenvs.create false \
    && cd /app \
    && poetry install --no-root --no-dev \
    && apk del .build-deps $BUILD_DEPS

COPY ./cli /app
