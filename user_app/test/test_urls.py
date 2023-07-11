from django.test import SimpleTestCase
from django.urls import reverse, resolve
from user_app.views import register,user_login

# To run a test the syntax is python manage.py test "App_name". In this case is python manage.py test user_app

class TestUrls(SimpleTestCase):

    def test_register_urls_resolves(self):
        url=reverse('user_app:register') # This name is taken from the urls name
        print(resolve(url))
        self.assertEquals(resolve(url).func,register) 
    
    
    def test_login_urls_resolves(self):
        url=reverse('user_app:login') # This name is taken from the urls name
        print(resolve(url))
        self.assertEquals(resolve(url).func,user_login) 
        