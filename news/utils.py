from newsapi import NewsApiClient
import os

from account.models import User
from .models import News, Category

API_KEY = os.environ.get('NEWS_API_KEY')


def fetch(date_from):
    client = NewsApiClient(api_key=API_KEY)
    for category in Category.objects.all():
        response = client.get_everything(q=category.name, language='en', from_param=date_from)
        articles = response.get('articles', [])
        if len(articles) == 0:
            print(f'No Articles found for {category.name}')
        for article in articles:
            db_news = News(
                title=article.get('title'),
                content=article.get('content').split("[")[0],
                image_url=article.get('urlToImage'),
                category=category,
                pub_date=article.get('published_at'),
                created_at=article.get('published_at'),
                created_by=User.objects.get(pk=1),
            )
            db_news.save()
            print('data saved')
