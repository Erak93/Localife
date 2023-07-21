from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from user_app.models import Experience, UserProfile, Review, Region
from search_app.models import Booking

class ReviewTestCase(TestCase):
    def setUp(self):
         # Create test users and user profiles
        self.user1 = User.objects.create_user(username='user1', password='password1')
        self.user_profile1 = UserProfile.objects.create(user=self.user1, user_bio="User 1 bio")

        self.user2 = User.objects.create_user(username='user2', password='password2')
        self.user_profile2 = UserProfile.objects.create(user=self.user2, user_bio="User 2 bio")

        # Create Test Region
        self.region = Region.objects.create(region_name="TestReg", region_desc="I am a test Region")

        # Create test experiences
        self.experience1 = Experience.objects.create(host=self.user_profile2,title='Experience 1', end_date='2023-06-30', price=100, region=self.region)
        self.experience2 = Experience.objects.create(host=self.user_profile1,title='Experience 2', end_date='2023-07-15', price= 50, region=self.region)

        # Create test bookings
        self.booking1 = Booking.objects.create(experience_name='Experience 1', traveler='user1', host='user2')
        self.booking2 = Booking.objects.create(experience_name='Experience 2', traveler='user2', host='user1')

    def test_create_review_valid_booking(self):
        # Ensure that the view allows review creation for valid bookings
        self.client.login(username='user1', password='password1')
        response = self.client.post(reverse('finished_app:create_review', args=[self.experience1.id]), {
            'rating': 5,
            'comment': 'This is a test review for Experience 1.',
        })

        #self.assertEqual(response.status_code, 200)
        if response:
            self.assertTemplateUsed('finished_app/thank_you.html')

        self.assertTrue(Review.objects.filter(author=self.user1.user_profile, listing=self.experience1).exists())

    def test_create_review_invalid_booking(self):
        # Ensure that the view disallows review creation for invalid bookings
        self.client.login(username='user2', password='password2')
        response = self.client.post(reverse('finished_app:create_review', args=[self.experience1.id]), {
            'rating': 5,
            'comment': 'This is a test review for Experience 1 with an invalid booking.',
        })
        #self.assertEqual(response.status_code, 200)
        if response:
            self.assertTemplateUsed('finished_app/review_not_allowed.html')

        self.assertFalse(Review.objects.filter(author=self.user2.user_profile, listing=self.experience1).exists())

    def test_create_review_untimely(self):
        # Ensure that the view disallows review creation for experiences with an end date in the future
        self.client.login(username='testuser1', password='testpassword1')
        response = self.client.post(reverse('finished_app:create_review', args=[self.experience2.id]), {
            'rating': 4,
            'comment': 'This is a test review for Experience 2, which is untimely.',
        })
        #self.assertEqual(response.status_code, 200)
        if response:
            self.assertTemplateUsed('finished_app/review_untimely.html')

        self.assertFalse(Review.objects.filter(author=self.user1.user_profile, listing=self.experience2).exists())