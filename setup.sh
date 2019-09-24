#!/bin/bash
# preliminary startup script, this is how configuration could look like
export DJANGO_SETTINGS_MODULE=sma_rest.settings.prod
export DB_NAME=postgres
export DB_USER=postgres
export DB_PASSWORD='mysecretpassword'
export DB_HOST=localhost DB_PORT=5432
export SECRET_KEY='n0kj%5^0!$9my(kv(keuub&j4s325^^swkjj@8ct&$7sxn2!a8'
python ./manage.py migrate --settings=sma_rest.settings.prod
python ./manage.py loaddata sma_rest/settings/admin/local_admin.json --settings=sma_rest.settings.prod
python ./manage.py runserver --settings=sma_rest.settings.prod