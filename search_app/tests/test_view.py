from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.shortcuts import render
from user_app.models import Experience
from search_app.filters import ExperienceFilter, SecondFilter, APIFilter
from search_app.serializers import ExperienceSerializer, APISerializer
from search_app.views import index, SearchAPIView

class IndexViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view(self):
        url = reverse('search_index')
        request = self.factory.get(url)
        response = index(request)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_app/search_app.html')
        self.assertIn('filter1', response.context)
        self.assertIn('filter2', response.context)

class SearchAPIViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_search_api_view(self):
        url = reverse('search_api')
        request = self.factory.get(url)
        response = SearchAPIView.as_view({'get': request})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.response_data, 'Expected response data')

        # Add additional assertions as needed

