# Generated by Django 4.1.4 on 2022-12-22 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_alter_activity_main_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='main_img',
            field=models.ImageField(upload_to='uploads/images'),
        ),
    ]
