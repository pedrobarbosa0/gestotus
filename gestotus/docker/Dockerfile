FROM python:3.7.7-alpine

WORKDIR /app

ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libmagic jpeg-dev zlib-dev libxml2-dev libxslt-dev

COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/

ENTRYPOINT ["/app/docker/entrypoint.sh"]