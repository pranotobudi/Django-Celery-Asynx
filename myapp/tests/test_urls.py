
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from myapp.views import home_view, generate_random_user_pull, PhotoView, check_progress_view

class TestUrls(SimpleTestCase):

    def test_home_url_resolve(self):
        url_path = reverse('home')
        print(url_path)
        self.assertEqual(resolve(url_path).func, home_view)

    def test_generate_random_user_pull_url_resolve(self):
        url_path = reverse('generate-random-user-pull')
        print(url_path)
        self.assertEqual(resolve(url_path).func, generate_random_user_pull)


    def test_load_flickr_images_pull_url_resolve(self):
        url_path = reverse('load-flickr-images-pull')
        print(url_path)
        self.assertEqual(resolve(url_path).func.view_class, PhotoView)

    def test_check_progress_view_url_resolve(self):
        url_path = reverse('check-progress-view')
        print(url_path)
        self.assertEqual(resolve(url_path).func, check_progress_view)
