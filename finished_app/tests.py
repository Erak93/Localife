from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from user_app.models import UserProfile
from search_app.models import  Booking
from user_app.models import Review,Experience

class ReviewTestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = Client()
        self.client.login(username='testuser', password='testpass')

        # Create a UserProfile for the traveler
        self.traveler_profile = UserProfile.objects.create(user=self.user, location='Location 1')


        # Create an experience
        self.experience = Experience.objects.create(
            title='Test Experience',
            description='This is a test experience description.',
            host=self.traveler_profile,
            price=100
            # Add other necessary fields as required for your model
        )

        # Create a booking for the experience
        self.booking = Booking.objects.create(
            traveler='testuser',
            host=self.user.username,
            experience_name=self.experience.title,
            # Add other necessary fields as required for your model
        )

    def test_create_review_valid_booking(self):
        # Ensure that the view creates a review for a valid booking
        response = self.client.post(reverse('finished_app:create_review', args=[self.experience.id]), {
            'rating': 5,
            'comment': 'This is a test review.',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finished_app/thank_you.html')

        # Check if the review is created in the database
        self.assertTrue(Review.objects.filter(author=self.user.user_profile, listing=self.experience).exists())

    def test_create_review_invalid_booking(self):
        # Ensure that the view redirects to 'review_not_allowed.html' for an invalid booking
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('finished_app:create_review', args=[self.experience.id]), {
            'rating': 5,
            'comment': 'This is a test review.',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'finished_app/review_not_allowed.html')

        # Check if the review is not created in the database
        self.assertFalse(Review.objects.filter(author=self.user.user_profile, listing=self.experience).exists())

    def test_create_review_not_authenticated(self):
        # Ensure that the view redirects to the login page for unauthenticated users
        self.client.logout()
        response = self.client.post(reverse('finished_app:create_review', args=[self.experience.id]), {
            'rating': 5,
            'comment': 'This is a test review.',
        })
        self.assertRedirects(response, f'/user/login/?next=/finished/reviews/create/{self.experience.id}/')

    # Add more test cases as needed for other scenarios


