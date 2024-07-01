from django.db import models
from django.utils import timezone
from datetime import timedelta

from account.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)
    display_in_home = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    @classmethod
    def get_home_categories(cls):
        categories = cls.objects.filter(display_in_home=True)
        return categories

    def get_trending_news(self):
        one_week_ago = timezone.now() - timedelta(days=7)
        return self.news_set.filter(pub_date__gte=one_week_ago).order_by('-views')[:3]

    def get_most_recent_news(self):
        return self.news_set.order_by('-pub_date')[:5]

    def get_most_popular_news(self):
        return self.news_set.order_by('-views')[:10]


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField()
    image_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['title']
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return f'{self.title}-{self.created_by.get_full_name()}'

    @classmethod
    def get_trending_news(cls):
        # for one week trending news
        # one_week_ago = timezone.now() - timedelta(days=7)
        # return cls.objects.filter(pub_date__gte=one_week_ago).order_by('-views')[:3]
        return cls.objects.order_by('-views')[:3]

    @classmethod
    def get_most_recent_news(cls):
        return cls.objects.order_by('-pub_date')[:10]

    @classmethod
    def get_most_popular_news(cls):
        return cls.objects.order_by('-views')[:10]



# class FanFollow(models.Model):
#     icon = models.ImageField()
#     name = models.CharField(max_length=255)
#     count = models.PositiveIntegerField(default=0)
#
# class SocialHandles(models.Model):
#     icon = models.ImageField()
#     name = models.CharField(max_length=255)
#     link = models.CharField(default=0)


# class Ads(models.Model):
#     title = models.CharField(max_length=255)
#     banner = models.ImageField()
#     location = models.CharField(max_length=255) // top_homepage , right_homepage, footer




