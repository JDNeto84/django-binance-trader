#!/bin/sh

PUBLIC_IP=$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4)

if [ -z "$PUBLIC_IP" ]; then
  PUBLIC_IP="localhost"
fi

export DJANGO_ALLOWED_HOSTS=$PUBLIC_IP

echo "DJANGO_ALLOWED_HOSTS set to:  $DJANGO_ALLOWED_HOSTS"

gunicorn --workers 3 --bind 0.0.0.0:8000 core.config.wsgi:application
