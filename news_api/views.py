
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView


from news.models import Category, News
from news_api.serializers import CategorySerializer, NewsSerializer


# Create your views here.

class CategoryViewSet(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NewsViewSet(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

# class CategoryViewSet(ReadOnlyModelViewSet):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
#
# class NewsViewSet(ReadOnlyModelViewSet):
#     queryset = News.objects.all()
#     serializer_class = NewsSerializer


