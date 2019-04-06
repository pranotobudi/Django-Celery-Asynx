import json
import requests

from myapp.models import Photo
from myapp import settings as photo_settings
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

def get_latest_flickr_image():
    """
    Grabs the latest image from the flick public image feed
    """
    url = photo_settings.FLICKR_JSON_FEED_URL
    r = requests.get(url)
    page_content = r.text
    # It turns out Flickr escapes single quotes (')
    # and apparently this isn't allowed and makes the JSON invalid.
    # we use String.replace to get around this
    probably_json = page_content.replace("\\'", "'")
    # now we load the json
    feed = json.loads(probably_json)
    images = feed['items']
    return images[0]


def save_latest_flickr_image():
    """
    We get the lastest image and save it to our Photo Model in the Database
    """
    logger.info("|||||||||||||||||||||||||||||||||||||||")
    logger.info("FUNCTION: save_latest_flickr_image")

    flickr_image = get_latest_flickr_image()
    # lets make sure we don't save the same image more than once
    # we are assuming each Flickr image has a unique Link
    if not Photo.objects.filter(link=flickr_image['link']).exists():
        photo = Photo(
            title=flickr_image['title'],
            link=flickr_image['link'],
            image_url=flickr_image['media']['m'],
            description=flickr_image['description']
        )
        length = len(Photo.objects.all())
        if(length >= 6):
            #delete last element, we only show 6 images
            earliest = Photo.objects.earliest('created_on')
            Photo.objects.filter(id=earliest.id).delete()
        photo.save()

