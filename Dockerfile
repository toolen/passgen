FROM python:3.6-alpine

LABEL maintainer="dmitry@zaharov.spb.ru"

COPY ./passgen /app
COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["gunicorn", "-w", "4", "app:application"]

EXPOSE 8000
