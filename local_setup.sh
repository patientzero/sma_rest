#!/bin/bash
python ./manage.py makemigrations --settings=sma_rest.settings.local
python ./manage.py migrate --settings=sma_rest.settings.local
# load local admin with credentials: base830 and password base830
python ./manage.py loaddata sma_rest/settings/admin/local_admin.json --settings=sma_rest.settings.local
export KALDI_ROOT='/home/luisparra/Documentos/'
export INTEL_ROOT='/home/'