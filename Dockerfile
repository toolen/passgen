FROM alpine:3.8

LABEL maintainer="dmitrii@zakharov.cc"

ENV PASSGEN_CORS_ENABLED="True"
ENV GUNICORN_CMD_ARGS="-b 0.0.0.0:80"

WORKDIR .

COPY ./passgen /passgen
COPY requirements/prod.txt requirements.txt

RUN apk add --no-cache \
        python3 && \
        pip3 install --no-cache-dir -r requirements.txt && \
        addgroup -S gunicorn && \
        adduser -S -G gunicorn gunicorn && \
        chown -R gunicorn:gunicorn passgen

CMD ["gunicorn", "-u", "gunicorn", "-g", "gunicorn", "passgen.app:application"]
