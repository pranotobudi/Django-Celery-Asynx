from django.contrib.auth.models import User
from celery import shared_task, current_task 
from django.utils.crypto import get_random_string
import string

@shared_task
def generate_user_task(total_user):
    for i in range(total_user):
        username = "username{}".format(get_random_string(10, string.ascii_letters))
        email = '{}@email.com'.format(username)
        password =  get_random_string(50)

        User.objects.create_user(username=username, email=email, password=password)
        current_task.update_state(state='PROGRESS', meta={
                                    'current': i,
                                    'total': total_user,
                                    'percent':int((i*100)/total_user),
                                })

    return {'current': total_user, 'total': total_user, 'percent': 100}

