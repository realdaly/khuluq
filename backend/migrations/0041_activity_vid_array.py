# Generated by Django 4.1.4 on 2023-01-03 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0040_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='vid_array',
            field=models.ManyToManyField(blank=True, related_name='activities', to='backend.video'),
        ),
    ]
