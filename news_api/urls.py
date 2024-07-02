from django.urls import path, include
from .views import CategoryViewSet, NewsViewSet


urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('categories', CategoryViewSet.as_view()),
    path('news', NewsViewSet.as_view())
]