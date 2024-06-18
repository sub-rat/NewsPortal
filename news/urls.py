from django.urls import path
from .views import AboutUsPageView, ContactPageView, LatestNewsPageView, CategoryPageView

urlpatterns = [
    path('about', AboutUsPageView.as_view(), name='about'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('latest', LatestNewsPageView.as_view(), name='latest_news'),
    path('category', CategoryPageView.as_view(), name='category'),
]
