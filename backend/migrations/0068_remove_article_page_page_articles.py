# Generated by Django 4.1.7 on 2023-05-05 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0067_remove_page_articles_remove_page_route_article_page_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='page',
        ),
        migrations.AddField(
            model_name='page',
            name='articles',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='backend.article'),
        ),
    ]
