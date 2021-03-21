FROM python:3.8.8-slim-buster

LABEL maintainer="dmitrii@zakharov.cc"

ENV \
    # Tell apt-get we're never going to be able to give manual feedback:
    DEBIAN_FRONTEND=noninteractive \
    # build:
    BUILD_ONLY_PACKAGES='wget' \
    # python:
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # tini:
    TINI_VERSION=v0.19.0 \
    # poetry:
    POETRY_VERSION=1.1.5 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.poetry/bin" \
    # passgen
    PASSGEN_CORS_ENABLED="True" \
    GUNICORN_CMD_ARGS="-b 0.0.0.0:8080"

# System deps:
RUN set -ex \
    # Update the package listing, so we know what package exist:
    && apt-get update \
    # Install security updates:
    && apt-get -y upgrade \
    # Install a new package, without unnecessary recommended packages:
    && apt-get install --no-install-recommends -y \
        # Defining build-time-only dependencies:
        $BUILD_ONLY_PACKAGES \
    # Installing `tini` utility:
    # https://github.com/krallin/tini
    && wget "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini" \
    && wget "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.sha256sum" \
    && sha256sum -c tini.sha256sum \
    && mv tini /usr/local/bin/tini \
    && chmod +x /usr/local/bin/tini \
    # Installing `poetry` package manager:
    # https://github.com/python-poetry/poetry
    && pip install --no-cache-dir poetry==${POETRY_VERSION} \
    # Removing build-time-only dependencies:
    && apt-get remove -y $BUILD_ONLY_PACKAGES \
    # Cleaning cache:
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf tini.sha256sum \
    # Setting up proper permissions:
    && groupadd -r passgen \
    && useradd -d /srv/passgen -r -g passgen passgen

COPY --chown=passgen:passgen ./poetry.lock ./pyproject.toml /srv/passgen/

WORKDIR /srv/passgen

# Project initialization:
RUN poetry install --no-dev --no-interaction --no-ansi \
    && rm -rf "$POETRY_CACHE_DIR"

COPY --chown=passgen:passgen ./passgen /srv/passgen/passgen/

# Running as non-root user:
USER passgen

CMD [ "/usr/local/bin/tini", "--", \
"gunicorn", \
"--worker-tmp-dir", "/dev/shm", \
"--worker-class", "aiohttp.worker.GunicornWebWorker", \
"--workers=2", \
"--threads=4", \
"--log-file=-", \
"--chdir", "/srv/passgen", \
"passgen.app:create_app"]