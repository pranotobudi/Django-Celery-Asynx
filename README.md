# "# Django-Celery-Asynx" 
## How to run this project:
### DEVELOPMENT (WINDOWS):
##### Change to development settings:
    manage.py, wsgi.py, celery.py
##### run celery worker: celery -A django_celery_asynx worker -l info -P gevent
##### run beat scheduler: celery -A django_celery_asynx beat -l info
##### run python: python manage.py runserver
### PRODUCTION:
##### Change to production settings:
    manage.py, wsgi.py, celery.py
##### see "Procfile"
