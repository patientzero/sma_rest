#!/bin/bash
set -euo pipefail

# stuff that should run before Django starts goes here
python ./manage.py makemigrations --settings=sma_rest.settings.$1
python ./manage.py migrate --settings=sma_rest.settings.$1
# load local admin with credentials: base830 and password base830
python ./manage.py loaddata sma_rest/settings/admin/local_admin.json --settings=sma_rest.settings.$1

exec $@
