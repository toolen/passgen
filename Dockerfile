FROM python:3.8.7-alpine3.12

LABEL maintainer="dmitrii@zakharov.cc"

ENV \
    # python:
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry:
    POETRY_VERSION=1.1.4 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.poetry/bin" \
    # passgen
    PASSGEN_CORS_ENABLED="True" \
    GUNICORN_CMD_ARGS="-b 0.0.0.0:8080"

RUN \
    set -ex \
    && apk add --no-cache \
        # Installing `tini` utility:
        # https://github.com/krallin/tini
        tini==0.19.0-r0 \
    && apk add --no-cache --virtual .build-deps \
        gcc==9.3.0-r2 \
        musl-dev==1.1.24-r10 \
        libffi-dev==3.3-r2 \
        libressl-dev==3.1.2-r0 \
    # Installing `poetry` package manager
    && pip install --no-cache-dir "poetry==$POETRY_VERSION" \
    # Setting up proper permissions:
    && addgroup -S passgen \
    && adduser -S -h /srv/passgen -G passgen passgen

COPY --chown=passgen:passgen ./poetry.lock ./pyproject.toml /srv/passgen/

WORKDIR /srv/passgen

# Project initialization:
RUN poetry install --no-dev --no-interaction --no-ansi \
    # Cleaning
    && rm -rf "$POETRY_CACHE_DIR" \
    && apk del .build-deps

COPY --chown=passgen:passgen ./passgen /srv/passgen/passgen/

# Running as non-root user:
USER passgen

CMD ["/sbin/tini", "--", "gunicorn", "--worker-class", "aiohttp.worker.GunicornWebWorker", "--chdir", "/srv/passgen", "passgen.app:create_app"]
