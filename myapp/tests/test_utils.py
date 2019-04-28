from django.test import SimpleTestCase, TestCase
from myapp.utils import get_latest_flickr_image
from unittest.mock import Mock
from unittest.mock import patch

# class TestUtils(TestCase):
    
#     @patch('myapp.utils.requests.get')
#     @patch('myapp.utils.requests.Response')
#     def test_get_latest_flickr_image_get(self, mock_flickr_response, mock_get):
#         expected_dict = {
#                 "title": "Uploads from everyone",
#                 "link": "https:\/\/www.flickr.com\/photos\/",
#                 "description": "",
#                 "modified": "2019-04-28T03:37:38Z",
#                 "generator": "https:\/\/www.flickr.com",
#                 "items": [
#             {
#                     "title": "Cow",
#                     "link": "https:\/\/www.flickr.com\/photos\/bpgrossphotography\/32775480097\/",
#                     "media": {"m":"https:\/\/live.staticflickr.com\/65535\/32775480097_8885a07d53_m.jpg"},
#                     "date_taken": "2014-06-03T17:47:00-08:00",
#                     "description": " <p><a href=\"https:\/\/www.flickr.com\/people\/bpgrossphotography\/\">BubbaPhotography<\/a> posted a photo:<\/p> <p><a href=\"https:\/\/www.flickr.com\/photos\/bpgrossphotography\/32775480097\/\" title=\"Cow\"><img src=\"https:\/\/live.staticflickr.com\/65535\/32775480097_8885a07d53_m.jpg\" width=\"240\" height=\"160\" alt=\"Cow\" \/><\/a><\/p> <p>#countryexploring #rural<\/p>",
#                     "published": "2019-04-28T03:37:38Z",
#                     "author": "nobody@flickr.com (\"BubbaPhotography\")",
#                     "author_id": "83894187@N04",
#                     "tags": "060314 2014 bpgrossphotography d7100 june minnesota minnesotaphotographer nikon nikond7100 nikonphotography outexploring outinthecountry raw ruralexploring cow"
#             },
#                 ]
#         }
#         mock_get.text = Mock(text=expected_dict).text
#         # mock_flickr_response.text = Mock(text=expected_dict).text
#         # mock_flickr_response.return_value = expected_dict
#         # mock_flickr_response.status_code = 200

#         #define response data for mock object
#         # mock_flickr_response.data = expected_dict
#         #call the real function, 
#         last_images = get_latest_flickr_image()
#         self.assertEqual(last_images['title'], 'Cow')
        

