FROM python:alpine3.20
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
RUN apk update && \
    apk add --no-cache nginx openssl mariadb-connector-c-dev && \
    add --no-cache --virtual .build-deps build-base mariadb-dev && \
    apk del .build-deps
COPY app /app
