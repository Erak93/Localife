from django.contrib.auth.models import User
from django.test import TestCase
from user_app.models import Experience,UserProfile
from post_app.forms import ExperienceForm

class ExperienceFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.experience = Experience.objects.create(title='Test Experience', description='Test description',
                                                    price=10.0, host=self.user_profile)

    def test_experience_form_valid(self):
        form_data = {
            'host': self.user_profile.id, #
            'title': 'Test Experience',
            'description': 'Test Description',
            'price': 10.0,
            # Add other required form fields here
        }
        form = ExperienceForm(data=form_data)
        self.assertTrue(form.is_valid())