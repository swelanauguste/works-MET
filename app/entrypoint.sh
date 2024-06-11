#!/bin/sh

# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $SQL_HOST $SQL_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi
# python manage.py flush --noinput
python manage.py migrate
python manage.py makemigrations
# python manage.py createsuperuser --username cworks --email ict.infrastructure@govt.lc --noinput
# python manage.py add_post
# python manage.py upload_data
python manage.py collectstatic --noinput

exec "$@"