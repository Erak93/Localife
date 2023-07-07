from django.test import TestCase
from user_app.forms import RegistrationForm,UserProfileForm
import tempfile

class TestForms(TestCase):
    def test_registration_form_valid_data(self):
        form=RegistrationForm(data={
            'password':'123456',
            'username':'test_user',
            'first_name':'test',
            'last_name':'user',
            'email':'test@user.com'
        })

        self.assertTrue(form.is_valid())
    
    def test_registration_form_partial_data(self):
        form=RegistrationForm(data={
            'username':'test_user',
            'first_name':'test',
            'last_name':'user',
            'email':'test@user.com'

        })

        self.assertFalse(form.is_valid()) # Testing if a form without password is false
    
    def test_registration_form_no_data(self):
        form=RegistrationForm(data={})

        self.assertFalse(form.is_valid()) # Testing if an empty form is false
    

    def test_user_profile_form_valid_data(self):
        form=UserProfileForm(data={
            'location':'Berlin',
            'user_profile_image':tempfile.NamedTemporaryFile(suffix=".jpg").name,

        })

        self.assertTrue(form.is_valid())
    
    def test_user_profile_form_partial_data_1(self):
        form=UserProfileForm(data={
            'location':'Berlin',
            

        })

        self.assertTrue(form.is_valid())
    
    def test_user_profile_form_partial_data_2(self):
        form=UserProfileForm(data={
            'user_profile_image':tempfile.NamedTemporaryFile(suffix=".jpg").name,
            

        })

        self.assertTrue(form.is_valid())
    
    def test_user_profile_form_valid_with_no_data(self):
        form=UserProfileForm(data={})

        self.assertTrue(form.is_valid())