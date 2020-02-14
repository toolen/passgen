FROM python:3.7.6-alpine3.11

LABEL maintainer="dmitrii@zakharov.cc"

ENV PASSGEN_CORS_ENABLED="True"
ENV GUNICORN_CMD_ARGS="-b 0.0.0.0:80"

WORKDIR .

COPY ./passgen /passgen
COPY requirements/requirements.txt requirements.txt

RUN pip install --require-hashes --no-cache-dir -r requirements.txt && \
    addgroup -S gunicorn && \
    adduser -S -G gunicorn gunicorn && \
    chown -R gunicorn:gunicorn passgen

CMD ["gunicorn", "-u", "gunicorn", "-g", "gunicorn", "passgen.app:application"]
