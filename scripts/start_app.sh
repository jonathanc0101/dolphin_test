#!/bin/bash
 python manage.py flush --no-input && python manage.py migrate --noinput && python manage.py collectstatic --noinput && python manage.py data_insert && gunicorn dolphin_site.wsgi -b 0.0.0.0:8000
