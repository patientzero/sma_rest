FROM python:3.7-stretch

# update pip and setuptools
RUN pip install -U pip setuptools

RUN apt-get update && apt-get --yes install \
        bash \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir uWSGI==2.0.17

COPY requirements.txt /tmp/
RUN pip install --no-cache-dir --prefer-binary -r /tmp/requirements.txt

ARG PROJECT_ROOT=/opt/project

ENV PYTHONPATH=${PROJECT_ROOT}

COPY . /opt/project
RUN mkdir /srv/appdata
RUN chown -R $USER:$USER /opt/project
RUN chown -R $USER:$USER /srv/appdata

WORKDIR /opt/project

# directories Django writes to
ENV \
  MEDIA_ROOT=/srv/appdata/media \
  STATIC_ROOT=/srv/appdata/static \
  SQLITE_DIR=/srv/appdata/sqlite
RUN mkdir $MEDIA_ROOT $STATIC_ROOT $SQLITE_DIR

# make uWSGI serve sta/tic files at /static
ENV UWSGI_STATIC_MAP="/static/=$STATIC_ROOT"

RUN ./manage.py collectstatic --settings=sma_rest.settings.local  --noinput

EXPOSE 8000
#VOLUME ["/srv/appdata/media", "/srv/appdata/static", "/srv/appdata/sqlite"]
ENTRYPOINT ['init-container.sh', 'dev']
CMD ["uwsgi", "uwsgi.ini"]
