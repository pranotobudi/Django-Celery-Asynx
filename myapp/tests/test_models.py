from myapp.models import Photo
from django.test import TestCase
import datetime

class TestModels(TestCase):
    def setUp(self):
        self.photo1 = Photo.objects.create(
            title = "title 1",
            link = "http://wwww.website.com",
            image_url = "http://wwww.website.com",
            description = 'description 1',
        )

    def test_photo_db_is_created(self):
        total = Photo.objects.all().count()
        self.assertEqual(total, 1) 