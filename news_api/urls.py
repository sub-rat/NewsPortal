from django.urls import path, include
from .views import CategoryViewSet, NewsViewSet

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('categories', CategoryViewSet.as_view({'get': 'list'})),
    path('news', NewsViewSet.as_view({'get': 'list'})),
    path('categories/<int:pk>', CategoryViewSet.as_view({'get': 'retrieve'})),
    path('news/<int:pk>', NewsViewSet.as_view({'get': 'retrieve'}))
]
