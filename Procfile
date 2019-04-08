web: gunicorn django_celery_asynx.wsgi --log-file -
release: python manage.py migrate
worker: python manage.py celery worker -B -l info
beat: python manage.py celery beat –loglevel=info