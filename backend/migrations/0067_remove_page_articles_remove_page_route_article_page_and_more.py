# Generated by Django 4.1.7 on 2023-05-05 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0066_alter_page_articles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='articles',
        ),
        migrations.RemoveField(
            model_name='page',
            name='route',
        ),
        migrations.AddField(
            model_name='article',
            name='page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='backend.page'),
        ),
        migrations.AddField(
            model_name='page',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]