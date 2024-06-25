FROM python:3.12-alpine3.20

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV MYSQL_CONFIG="/usr/bin/mysql_config"

WORKDIR /app

RUN apk update && \
    apk add --no-cache \
    gcc \
    musl-dev \
    mysql-dev \
    mysql-client \
    python3-dev \
    libffi-dev \
    nginx \
    openssl \
    bash \
    curl

COPY requirements.txt /app/
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY app /app
COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/default.conf
RUN chmod +x /app/generate_cert.sh 
RUN /bin/sh /app/generate_cert.sh
RUN chmod +x /app/entrypoint.sh
EXPOSE 443 8000

ENTRYPOINT ["/bin/sh", "-c", ". /app/entrypoint.sh & nginx -g 'daemon off;'"]
