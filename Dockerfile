FROM python:3.6-alpine

LABEL maintainer="dmitry@zakharov.spb.ru"

COPY ./passgen /passgen
COPY requirements.txt .

WORKDIR .

RUN pip install -r requirements.txt

CMD ["gunicorn", "-b", "0.0.0.0:80", "passgen.app:application"]

EXPOSE 80
