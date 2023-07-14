import django_filters
from user_app.models import Experience


        

class ExperienceFilter(django_filters.FilterSet):
    #price = django_filters.NumberFilter()
    #price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    #price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    
    #start_date = django_filters.NumberFilter(field_name='start_date', lookup_expr='day')
    #end_date = django_filters.NumberFilter(field_name='end_date', lookup_expr='day')
    region = django_filters.CharFilter(field_name="region__region_name", lookup_expr="exact")
    #host__username = django_filters.CharFilter(lookup_expr='iexact')
    experience_tag = django_filters.CharFilter(field_name="experience_tags__tag_name", lookup_expr='contains')
    class Meta:
        model = Experience
        fields = []

class SecondFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    
    start_date = django_filters.NumberFilter(field_name='start_date', lookup_expr='day')
    end_date = django_filters.NumberFilter(field_name='end_date', lookup_expr='day')
    #region__region_name = django_filters.CharFilter(field_name="region", lookup_expr="iexact")
    host__username = django_filters.CharFilter(field_name='host__username',lookup_expr='exact')
    #experience_tag__tag_name = django_filters.CharFilter(field_name="experience_tags", lookup_expr='icontains')
    class Meta:
        model = Experience
        fields = []

    def filter_queryset(self, queryset):
        # Get the filtered queryset from the first filter
        filtered_queryset = super().filter_queryset(queryset)

        # Apply the second filter on the filtered queryset
        return super().filter_queryset(filtered_queryset)
    
from django_filters import rest_framework as drfilters

class APIFilter(drfilters.FilterSet):
    price = django_filters.NumberFilter()
    #price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    #price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    
    start_date = django_filters.NumberFilter(field_name='start date', lookup_expr='day')
    end_date = django_filters.NumberFilter(field_name='end date', lookup_expr='day')
    region = django_filters.CharFilter(field_name="region__region_name", lookup_expr="iexact")
    host = django_filters.CharFilter(field_name='host__username', lookup_expr='iexact')
    experience_tag = django_filters.CharFilter(field_name="experience tags__tag_name", lookup_expr='icontains')
    class Meta:
        model = Experience
        fields = ['price', 'start_date', 'end_date', 'region', 'host', 'experience_tags']