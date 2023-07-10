from django.test import SimpleTestCase
from django.urls import reverse, resolve
from post_app.views import test_view, create_experience, experience_list, experience_detail, post_list, post_create, post_detail, post_update  

class TestUrls(SimpleTestCase):

    def test_list_url_is_resolved(self):
        url = reverse('post_app:post_list')
        self.assertEquals(resolve(url).func, post_list)

    def test_create_url_is_resolved(self):
        url = reverse('post_app:post_create')
        self.assertEquals(resolve(url).func, post_create)

    def test_detail_url_is_resolved(self):
        url = reverse('post_app:post_detail', args=[1])
        self.assertEquals(resolve(url).func, post_detail)

    def test_update_url_is_resolved(self):
        url = reverse('post_app:post_update', args=[1])
        self.assertEquals(resolve(url).func, post_update)