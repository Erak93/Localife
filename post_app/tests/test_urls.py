from django.test import SimpleTestCase
from django.urls import reverse, resolve
from post_app.views import test_view, create_experience, experience_list, experience_detail  


class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('post_app:post_list')
        self.assertEquals(resolve(url).func, experience_list)

    def test_create_url_is_resolved(self):
        url = reverse('post_app:post_create')
        self.assertEquals(resolve(url).func, create_experience)

    def test_detail_url_is_resolved(self):
        url = reverse('post_app:post_detail', args=[1])
        self.assertEquals(resolve(url).func, experience_detail)