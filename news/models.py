from django.db import models

from account.models import User


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField()
    image_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'News'
        verbose_name_plural = 'News'

    def __str__(self):
        return f'{self.title}-{self.created_by.get_full_name()}'



