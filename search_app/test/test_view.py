from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from django.shortcuts import render
from user_app.models import Experience
from search_app.filters import ExperienceFilter, SecondFilter, APIFilter
from search_app.serializers import ExperienceSerializer, APISerializer
from search_app.views import index, SearchAPIView
from rest_framework import status

class IndexViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_index_view(self):
        url = reverse('search_app:search_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_app/search_app.html')
        self.assertIn('filter1', response.context)
        self.assertIn('filter2', response.context)

class SearchAPIViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_search_api_view(self):
        url = reverse('search_app:api-list')
        request = self.factory.get(url)
        view = SearchAPIView.as_view({'get': 'list'})  # Specify the actions argument
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        experiences = Experience.objects.all().order_by('region')
        serializer = APISerializer(experiences, many=True)
        expected_data = serializer.data

        self.assertEqual(response.data, expected_data)

        # Add additional assertions as needed