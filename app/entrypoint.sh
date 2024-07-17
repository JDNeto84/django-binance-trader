#!/bin/sh
if [ -f /sys/hypervisor/uuid ] && [ "$(head -c 3 /sys/hypervisor/uuid)" = "ec2" ]; then
  PUBLIC_IP=$(curl -s http://169.254.169.254/latest/meta-data/public-ipv4)
else
  PUBLIC_IP="localhost"
fi

if [ -z "$DJANGO_SECRET_KEY" ]; then
  DJANGO_SECRET_KEY="django-insecure-n25y9@^wmbwk@)1(9&(oyi@2q0_c&qikvq@@hy0v4s=g4y#t+5"
fi

export DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY
# export DJANGO_ALLOWED_HOSTS=$PUBLIC_IP      //Disabled to not initially use an EBS in AWS

gunicorn --workers 3 --bind 0.0.0.0:8000 core.config.wsgi:application &

daphne -b 0.0.0.0 -p 8001 core.config.asgi:application
