# Generated by Django 5.0.6 on 2024-07-01 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_news_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='display_in_home',
            field=models.BooleanField(default=False),
        ),
    ]