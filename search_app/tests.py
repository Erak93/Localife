from django.test import TestCase, RequestFactory
from django.urls import reverse
from .filters import ExperienceFilter 
from user_app.models import Experience

class MyFilterTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_filtering(self):
        # Create some test data
        Experience.objects.create(title='Item 1', host='A')
        Experience.objects.create(title='Item 2', host='B')
        Experience.objects.create(title='Item 3', host='A')
        
        # Set up the filter
        data = {'category': 'A'}
        request = self.factory.get(reverse('my_filter_view'), data=data)
        filter_instance = ExperienceFilter(request.GET, queryset=Experience.objects.all())
        
        # Apply the filter
        filtered_queryset = filter_instance.qs
        
        # Assert the expected results
        self.assertEqual(filtered_queryset.count(), 2)
        self.assertQuerysetEqual(
            filtered_queryset,
            ['<MyModel: Item 1>', '<MyModel: Item 3>'],
            ordered=False
        )
