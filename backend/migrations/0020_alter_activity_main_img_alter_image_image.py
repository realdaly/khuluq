# Generated by Django 4.1.4 on 2022-12-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_alter_activity_main_img_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='main_img',
            field=models.ImageField(upload_to='static/images'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
    ]
