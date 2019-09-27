#!/bin/bash
set -euo pipefail

# stuff that should run before Django starts goes here
python ./manage.py makemigrations --settings=sma_rest.settings
python ./manage.py migrate --settings=sma_rest.settings
# load local admin with credentials: base830 and password base830
DB_FILE=/srv/appdata/sqlite/db.sqlite
if [ -f "$DB_FILE" ]; then
  echo "$DB_FILE exists, doing nothing"
else
  echo "$DB_FILE does not exist, creating first user"
  python ./manage.py loaddata sma_rest/admin/local_admin.json
fi


exec $@
