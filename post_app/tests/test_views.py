from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from post_app.forms import Experience
from user_app.models import UserProfile
from rest_framework import status
from rest_framework.test import APIClient
from post_app.serializers import ExperienceSerializer

class TestView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.experience = Experience.objects.create(title='Test Experience', description='Test description',
                                                    price=10.0, host=self.user_profile)

    def test_create_experience(self):
        url = reverse('post_app:post_create')  
        data = {
            'title': 'New Experience',
            'description': 'New description',
            'price': 20.0,
            'host': self.user.user_profile.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'post_app/test_view.html')

        self.assertTrue(Experience.objects.filter(title='New Experience').exists())

class TestListView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('post_app:experience_list')
        self.user = User.objects.create(username='testuser')
        self.user_profile = UserProfile.objects.create(user=self.user)
        self.experience = Experience.objects.create(title='Test Experience', description='Test Description', price=10.0, host=self.user_profile)
    def test_experience_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        experiences = Experience.objects.all()
        serializer = ExperienceSerializer(experiences, many=True)
        self.assertEqual(response.data, serializer.data)


    def test_experience_detail_view(self):
        self.url = reverse('post_app:post_detail', args=[self.experience.id])
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        experience = Experience.objects.get(id=self.experience.id)
        serializer = ExperienceSerializer(experience, many=False)
        self.assertEqual(response.data, serializer.data)
    
    def test_delete_experience(self):
        self.url = reverse('post_app:post_detail', args=[self.experience.id])
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Experience.objects.filter(id=self.experience.id).exists())

    def test_update_experience(self):
        self.url = reverse('post_app:post_detail', args=[self.experience.id])
        data = {
            'title': 'New Experience',
            'description': 'New description',
            'price': 20.0,
            'host': self.user.user_profile.id
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Experience.objects.filter(title='New Experience').exists())
        self.assertFalse(Experience.objects.filter(title='Test Experience').exists())
        experience = Experience.objects.get(id=self.experience.id)
        serializer = ExperienceSerializer(experience, many=False)
        self.assertEqual(response.data, serializer.data)