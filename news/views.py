import datetime

from django.http import HttpResponse
from django.utils import timezone

from django.core.serializers.json import Serializer
from django.views.generic import TemplateView

from news.models import News, Category


# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trending'] = News.get_trending_news()  # News.objects.all().order_by('-pub_date')[:3]
        context['right_content'] = News.objects.all().order_by('-pub_date')[3:5]
        categories = Category.get_home_categories()
        context['news'] = {}
        context['categories'] = []
        for category in categories:
            news = category.get_most_recent_news()
            if news:
                context['categories'].append(category)
                context['news'][category.name] = news

        popular_news = News.get_most_popular_news()[:3]
        data = []
        for news in popular_news:
            data.append({
                'title': news.title,
                'created_by': news.created_by.get_full_name(),
                'id': news.id,
                'image': news.image.url if news.image else '',
                'image_url': news.image_url,
                'duration': f'{(timezone.now() - news.created_at).total_seconds() / 3600:.1f} hour',
            })
        self.request.session['popular'] = data
        return context

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.cookies['name'] = 'subrat gyawali'
        response.cookies['test'] = 'value'
        set_cookie(
            response=response,
            key="COOKIE_KEY",
            value="COOKIE_VALUE",
            cookie_host=request.get_host(),
            days_expire=7,
        )
        return response


class CategoryPageView(TemplateView):
    template_name = 'category.html'


class AboutUsPageView(TemplateView):
    template_name = 'about.html'


class ContactPageView(TemplateView):
    template_name = 'contact.html'


class LatestNewsPageView(TemplateView):
    template_name = 'latest_news.html'


class DetailPageView(TemplateView):
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        detail = News.objects.get(pk=self.kwargs['pk'])
        detail.views += 1
        detail.save()
        context['news'] = detail
        return context


def set_cookie(
        response: HttpResponse,
        key: str,
        value: str,
        cookie_host: str,
        days_expire: int = 365,
):
    max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(days=days_expire), "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    domain = cookie_host.split(":")[0]
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires,
        domain=domain,
        secure=False,
    )
