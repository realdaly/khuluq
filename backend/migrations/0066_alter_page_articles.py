# Generated by Django 4.1.7 on 2023-05-05 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0065_article_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='articles',
            field=models.ManyToManyField(related_name='articles', to='backend.article'),
        ),
    ]
