FROM alpine:latest

LABEL maintainer="dmitrii@zakharov.cc"

COPY ./passgen /passgen
COPY requirements/prod.txt requirements.txt

WORKDIR .

RUN apk add --no-cache \
        python3 && \
        pip3 install --no-cache-dir -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:80", "passgen.app:application"]

EXPOSE 80
