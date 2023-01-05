# Generated by Django 4.1.4 on 2023-01-04 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0044_remove_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='img_array',
            field=models.ManyToManyField(blank=True, related_name='images', to='backend.image'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='main_img',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='mainImage', to='backend.image'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='vid_array',
            field=models.ManyToManyField(blank=True, related_name='videos', to='backend.video'),
        ),
    ]