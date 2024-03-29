FROM python:3.10.9-slim-bullseye@sha256:6862d8ed663a47f649ba5aababed01e44741a032e80d5800db619f5113f65434 AS builder

LABEL maintainer="dmitrii@zakharov.cc"
LABEL org.opencontainers.image.source="https://github.com/toolen/passgen"

ENV \
    DEBIAN_FRONTEND=noninteractive \
    # python:
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # poetry:
    POETRY_VERSION=1.1.12 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=true \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    PATH="$PATH:/root/.local/bin"

RUN pip install --no-cache-dir poetry==$POETRY_VERSION

WORKDIR /code

COPY ./poetry.lock ./pyproject.toml /code/

RUN poetry export --no-ansi --no-interaction --output requirements.txt

FROM python:3.10.9-alpine3.17@sha256:d8a484baabf7d2337d34cdef6730413ea1feef4ba251784f9b7a8d7b642041b3 AS runner

LABEL maintainer="dmitrii@zakharov.cc"
LABEL org.opencontainers.image.source="https://github.com/toolen/passgen"

ENV \
    # python:
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    # pip:
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # passgen
    PASSGEN_CORS_ENABLED="True" \
    # gunicorn
    GUNICORN_CMD_ARGS="--workers=2 --threads=4"

RUN set -ex \
    && apk upgrade \
    && apk add --no-cache \
        tini==0.19.0-r1 \
    && addgroup -g 1000 -S app \
    && adduser -h /app -G app -S -u 1000 app

COPY --chown=app:app --from=builder /code/requirements.txt /app

WORKDIR /app

USER app

RUN set -ex \
    && python -m venv venv \
    && venv/bin/pip install --no-cache-dir --require-hashes -r requirements.txt

COPY --chown=app:app ./passgen /app/passgen

COPY --chown=app:app ./healthcheck.py /app/passgen

WORKDIR /app/passgen

EXPOSE 8080

HEALTHCHECK --interval=5s --timeout=10s --retries=3 CMD /app/venv/bin/python healthcheck.py || exit 1

CMD ["/sbin/tini", "--", \
"/app/venv/bin/gunicorn", \
"--worker-tmp-dir", "/dev/shm", \
"--worker-class", "aiohttp.worker.GunicornWebWorker", \
"--log-file=-", \
"--chdir", "/app", \
"--bind", "0.0.0.0:8080", \
"passgen.app:create_app"]