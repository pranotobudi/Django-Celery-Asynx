import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from myapp.utils import save_latest_flickr_image
from celery import shared_task, current_task, task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

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

@task(name="photos.tasks.task_save_latest_flickr_image")
def task_save_latest_flickr_image():
    """
    Saves latest image from Flickr
    """
    save_latest_flickr_image()
    logger.info("|||||||||||||||||||||||||||||||||||||||")
    logger.info("PERIODIC TASK: SAVE IMAGE FROM FLICKR Saved image from Flickr")
     
