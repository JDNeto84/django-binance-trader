#!/bin/sh
gunicorn --workers 3 --bind 0.0.0.0:8000 core.config.wsgi:application