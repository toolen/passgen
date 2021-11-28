FROM python:3.10.0-slim-bullseye@sha256:3524d9553dd1ea815d9e3ff07a0ccafe878a9403fb5f9956dc6ad86075ac345f

LABEL maintainer="dmitrii@zakharov.cc"

ENV \
    # Tell apt-get we're never going to be able to give manual feedback:
    DEBIAN_FRONTEND=noninteractive \
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
    POETRY_VERSION=1.1.12 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.poetry/bin" \
    # passgen
    PASSGEN_CORS_ENABLED="True" \
    GUNICORN_CMD_ARGS=""

# System deps:
RUN set -ex \
    # Update the package listing, so we know what package exist:
    && apt-get update \
    # Install security updates:
    && apt-get -y upgrade \
    # Install a new package, without unnecessary recommended packages:
    && apt-get install --no-install-recommends -y \
        curl=7.74.0-1.3+b1 \
    # Installing `tini` utility:
    # https://github.com/krallin/tini
    && curl -OL "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini" \
    && curl -OL "https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini.sha256sum" \
    && sha256sum -c tini.sha256sum \
    && mv tini /usr/local/bin/tini \
    && chmod +x /usr/local/bin/tini \
    # Upgrading pip
    && pip install --no-cache-dir -U pip==21.3.1 \
    # Installing `poetry` package manager:
    # https://github.com/python-poetry/poetry
    && pip install --no-cache-dir poetry==${POETRY_VERSION} \
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

EXPOSE 8080

HEALTHCHECK --interval=5s --timeout=10s --retries=3 CMD curl -sS http://127.0.0.1:8080/api/v1/health || exit 1

CMD [ "/usr/local/bin/tini", "--", \
"gunicorn", \
"--worker-tmp-dir", "/dev/shm", \
"--worker-class", "aiohttp.worker.GunicornWebWorker", \
"--workers=2", \
"--threads=4", \
"--log-file=-", \
"--chdir", "/srv/passgen", \
"--bind", "0.0.0.0:8080", \
"passgen.app:create_app"]