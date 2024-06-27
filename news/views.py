from django.shortcuts import render
from django.views.generic import TemplateView

from news.models import News, Category


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trending'] = News.objects.all().order_by('-pub_date')[:3]
        context['right_content'] = News.objects.all().order_by('-pub_date')[3:5]
        # return context
        categories = Category.objects.all()[:6]
        context['news'] = {}
        context['categories'] = []
        for category in categories:
            news = News.objects.filter(category=category.id).order_by('-pub_date')[:5]
            if news:
                context['categories'].append(category)
                context['news'][category.name] = news
        return context


class CategoryPageView(TemplateView):
    template_name = 'category.html'


class AboutUsPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class LatestNewsPageView(TemplateView):
    template_name = 'latest_news.html'
