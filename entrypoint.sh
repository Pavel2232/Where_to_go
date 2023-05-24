#!/bin/bash
python manage.py migrate --check
status=$?
if [[ $status != 0 ]]; then
  python manage.py makemigrations
  python manage.py migrate
  python manage.py collectstatic
fi
exec "$@"