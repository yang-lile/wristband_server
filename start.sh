#!/bin/bash
# uwsgi --ini /var/www/html/wrist_band/uwsgi.ini
python manage.py makemigrations &&
python manage.py migrate &&
python manage.py runserver 0.0.0.0:8000
