web: gunicorn django_celery_asynx.wsgi --log-file -
release: python manage.py migrate
worker: celery -A django_celery_asynx worker -l info
beat: celery -A django_celery_asynx beat -l info 