import django_filters
from news.models import News


class NewsFilter(django_filters.FilterSet):
    views_gte = django_filters.NumberFilter(field_name='views', lookup_expr='gte')
    views_lte = django_filters.NumberFilter(field_name='views', lookup_expr='lte')
    published_gte = django_filters.DateTimeFilter(field_name='pub_date', lookup_expr='gte')
    published_lte = django_filters.DateTimeFilter(field_name='pub_date', lookup_expr='lte')
    category = django_filters.AllValuesFilter(field_name='category__name')

    class Meta:
        model = News
        fields = [
            'category',
            'views_gte',
            'views_lte',
            'published_gte',
            'published_lte',
        ]
