# Generated by Django 4.1.4 on 2022-12-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0008_image_section_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='main_img',
            field=models.FileField(upload_to='uploads/images'),
        ),
    ]