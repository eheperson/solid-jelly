#!/bin/sh

# entrypoint.sh file  : 
#    to verify that Postgres is healthy before applying the migrations 
#    and running the Django development server

if [ "$DATABASE" = "postgres" ]
then
    # check if postgre container is healthy
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      echo $SQL_HOST 
      echo $SQL_PORT 
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ "$MIGRATIONS" = "1" ]; then
#	python manage.py collectstatic --noinput
    python manage.py flush --no-input
    python manage.py migrate --noinput
	python manage.py createsuperuser --username "$DJANGO_SUPERUSER_NAME" --no-input --email "$DJANGO_SUPER_USER_EMAIL" 
    python manage.py runserver 0.0.0.0:8006
fi

exec "$@"