FROM python:3.12-alpine
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

RUN apk add --no-cache \
        nodejs \
        npm \
        postgresql-dev \
        gcc \
        curl \
        curl-dev \
        libcurl \
        musl-dev \
        libffi-dev \
        openldap-dev \
        ca-certificates \
        bash

RUN addgroup --gid=1000 cabot && adduser -G cabot -S -h /code -s /bin/bash cabot
RUN chown -R cabot:cabot /code

RUN npm install -g --registry http://registry.npmjs.org/ \
        coffee-script \
        less@1.3

ENV UV_PROJECT_ENVIRONMENT="/usr/local/"
ENV UV_COMPILE_BYTECODE=1
ENV UV_LOCKED=1
COPY pyproject.toml uv.lock ./
RUN uv sync --no-cache --all-extras

COPY --chown=cabot:cabot requirements-plugins.txt ./
RUN pip install --no-cache-dir -r requirements-plugins.txt

COPY --chown=cabot:cabot . /code

USER cabot
ENTRYPOINT ["./docker-entrypoint.sh"]
