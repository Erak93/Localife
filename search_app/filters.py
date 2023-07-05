import django_filters
from user_app.models import Experience


        

class ExperienceFilter(django_filters.FilterSet):
    #price = django_filters.NumberFilter()
    #price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    #price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    
    #start_date = django_filters.NumberFilter(field_name='start_date', lookup_expr='day')
    #end_date = django_filters.NumberFilter(field_name='end_date', lookup_expr='day')
    region__region_name = django_filters.CharFilter(field_name="region", lookup_expr="iexact")
    #host__username = django_filters.CharFilter(lookup_expr='iexact')
    experience_tag__tag_name = django_filters.CharFilter(field_name="experience_tags", lookup_expr='icontains')
    class Meta:
        model = Experience
        fields = ['region', 'experience_tags']

class SecondFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    
    start_date = django_filters.NumberFilter(field_name='start_date', lookup_expr='day')
    end_date = django_filters.NumberFilter(field_name='end_date', lookup_expr='day')
    #region__region_name = django_filters.CharFilter(field_name="region", lookup_expr="iexact")
    host__username = django_filters.CharFilter(lookup_expr='iexact')
    #experience_tag__tag_name = django_filters.CharFilter(field_name="experience_tags", lookup_expr='icontains')
    class Meta:
        model = Experience
        fields = ['price', 'start_date', 'host']