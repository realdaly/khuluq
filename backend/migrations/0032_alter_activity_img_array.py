# Generated by Django 4.1.4 on 2022-12-27 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0031_remove_image_section_activity_img_array'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='img_array',
            field=models.ManyToManyField(blank=True, to='backend.image'),
        ),
    ]
