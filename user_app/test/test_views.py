from django.test import TestCase
from django.urls import reverse
from user_app.models import User
from django.http import HttpResponseRedirect

class TestViews(TestCase):
    def test_register_view_post_valid_form(self):
        # Create a valid registration form data
        form_data = {
            'username': 'testuser',
            'password': 'testpassword',
            # Include other required fields from your RegistrationForm
        }

        # Send a POST request to the register view with the form data
        response = self.client.post(reverse('user_app:register'), data=form_data)

        # Check if the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # Check if the user was created in the database
        self.assertTrue(User.objects.filter(username='testuser').exists())

        # Add more assertions if needed

    def test_register_view_post_existing_username(self):
        # Create a user with the same username as the one we'll use in the form
        User.objects.create_user(username='testuser', password='testpassword')

        # Create registration form data with the existing username
        form_data = {
            'username': 'testuser',
            'password': 'newpassword',
            # Include other required fields from your RegistrationForm
        }

        # Send a POST request to the register view with the form data
        response = self.client.post(reverse('user_app:register'), data=form_data)

        # Check if the response status code is 200 (success)
        self.assertEqual(response.status_code, 200)

        # Check if the user was not created in the database
        users_with_username = User.objects.filter(username='testuser')
        self.assertEqual(users_with_username.count(), 1)

        # Add more assertions if needed
    

   
    def setUp(self):
        self.user = User.objects.create_user(username='test_login_user', password='test_login_password')

    def test_user_login_valid_credentials(self):
        # Create login form data with valid credentials
        form_data = {
            'username': 'test_login_user',
            'password': 'test_login_password',
        }

        # Send a POST request to the login view with the form data
        response = self.client.post(reverse('user_app:login'), data=form_data)

        # Check if the user was successfully logged in
        self.assertTrue(response.url.endswith(reverse('home_app')))  # Replace 'home_app' with the correct URL name
        self.assertEqual(response.status_code, 302)  # Check for a redirect

    def test_user_login_invalid_credentials(self):
        # Create login form data with invalid credentials
        form_data = {
            'username': 'test_login_user',
            'password': 'wrongpassword',
        }

        # Send a POST request to the login view with the form data
        response = self.client.post(reverse('user_app:login'), data=form_data)

        # Check if the login failed and an error message is displayed
        self.assertContains(response, "Invalid login details supplied!")
        self.assertEqual(response.status_code, 200)  # Check for a success response

    def test_user_login_inactive_account(self):
        # Deactivate the user account
        self.user.is_active = False
        self.user.save()

        # Create login form data with valid credentials
        form_data = {
            'username': 'test_login_user',
            'password': 'test_login_password',
        }

        # Send a POST request to the login view with the form data
        response = self.client.post(reverse('user_app:login'), data=form_data)

        # Check if the login fails due to an inactive account
        self.assertEqual(response.status_code, 200)  # Check for a success response
        self.assertTemplateUsed('templates/user_app/login.html') # If the user is not active the screen should remain on the login page  