from django.test import TestCase, SimpleTestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        client = Client()

    def test_home_view_get(self):
        url_path = reverse('home')
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/home.html')

    def test_generate_random_user_pull_get(self):
        url_path = reverse('generate-random-user-pull')
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/generate_random_user_pull.html')



    def test_load_flickr_images_pull_get(self):
        url_path = reverse('load-flickr-images-pull')
        response = self.client.get(url_path)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myapp/photo_list.html')



    def test_check_progress_view_get(self):
        url_path = reverse('check-progress-view')
        response = self.client.get(url_path)
        print(response)
        self.assertEqual(response.status_code, 200)
