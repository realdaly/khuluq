# Generated by Django 4.1.4 on 2023-01-03 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0042_audio_image_title_alter_image_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='audio',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]