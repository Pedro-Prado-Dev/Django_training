#!/bin/sh

cd /code

python manage.py migrate --settings=proj.settings_production
python manage.py runserver --settings=proj.settings_production