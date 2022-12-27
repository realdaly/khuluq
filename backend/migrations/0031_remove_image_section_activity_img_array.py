# Generated by Django 4.1.4 on 2022-12-23 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0030_remove_activity_img_array_image_section'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='section',
        ),
        migrations.AddField(
            model_name='activity',
            name='img_array',
            field=models.ManyToManyField(to='backend.image'),
        ),
    ]
