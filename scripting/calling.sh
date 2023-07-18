#!/bin/bash

set -e

python manage.py checkdb --settings=settings.development
python manage.py makemigrations --settings=settings.development
python manage.py migrate --settings=settings.development
python manage.py collectstatic --no-input --settings=settings.development
python manage.py createuser --settings=settings.development

echo "========================================="
echo "RIZAL, YOUR PROJECT IS UP AND RUNNING NOW"
echo "========================================="

export DJANGO_SETTINGS_MODULE=settings.development

daphne core.asgi:application -p 8000 -b 0.0.0.0