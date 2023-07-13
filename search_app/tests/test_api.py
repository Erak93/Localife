# ...
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from user_app.models import Experience, UserProfile, ExperienceTag, Region
from search_app.serializers import APISerializer
from search_app.views import SearchAPIView

class SearchAPIViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create some test objects
        region = Region.objects.create(region_name='Region A')
        user_profile = UserProfile.objects.create(username='user1')
        experience_tag = ExperienceTag.objects.create(tag_name='Tag 1')

        # Create some test experiences
        experience1 = Experience.objects.create(title='Experience 1', description='Description 1', start_date='2023-07-01',
                                  end_date='2023-07-05', price=100.00, region=region, host=user_profile)
        experience2 = Experience.objects.create(title='Experience 2', description='Description 2', start_date='2023-07-10',
                                  end_date='2023-07-15', price=200.00, region=region, host=user_profile
                                  )
        experience1.experience_tags.set([experience_tag])
        experience2.experience_tags.set([experience_tag])

    def test_search_experiences_by_region(self):
        url = reverse('search_app:api-list')
        region = "Region A"

        response = self.client.get(url, {'region': region})
        experiences = Experience.objects.filter(region__region_name=region)
        serializer = APISerializer(experiences, many=True)
        

        print("Response data:", response.data)
        print("Serializer data:", serializer.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


    def test_search_experiences_no_results(self):
        url = reverse('search_app:api-list')
        region_id = 2  # Assuming the region ID is 2

        response = self.client.get(url, {'region': region_id})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_list_all_experiences(self):
        url = reverse('search_app:api-list')

        response = self.client.get(url)
        experiences = Experience.objects.all()
        serializer = APISerializer(experiences, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
