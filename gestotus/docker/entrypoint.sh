#!/bin/sh

python ./manage.py collectstatic --noinput
python ./manage.py makemigrations
python ./manage.py migrate

gunicorn gestotus.wsgi -c config/gunicorn/gunicorn.conf.py
