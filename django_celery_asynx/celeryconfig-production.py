CELERY_BROKER_URL = 'amqp://qdgzpakt:abjU0ZWeBWyI48SG6SwQTLOe_hJzRWYg@orangutan.rmq.cloudamqp.com/qdgzpakt'
# CELERY_RESULT_BACKEND = 'amqp://qdgzpakt:abjU0ZWeBWyI48SG6SwQTLOe_hJzRWYg@orangutan.rmq.cloudamqp.com/qdgzpakt'
CELERY_RESULT_BACKEND = None
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_IMPORT = ('myapp',)
CELERY_BROKER_POOL_LIMIT = 1 #for heroku free dyno