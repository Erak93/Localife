from django.test import SimpleTestCase
from django.urls import reverse, resolve
from search_app.views import index, SearchAPIView

class UrlsTest(SimpleTestCase):
    def test_search_index_url(self):
        url = reverse('search_app:search_index')
        self.assertEqual(resolve(url).func, index)
        
    def test_search_api_url(self):
        url = reverse('search_app:api-list')
        self.assertEqual(resolve(url).func.__name__, SearchAPIView.__name__)

