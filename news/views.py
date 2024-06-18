from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'


class CategoryPageView(TemplateView):
    template_name = 'category.html'


class AboutUsPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class LatestNewsPageView(TemplateView):
    template_name = 'latest_news.html'
