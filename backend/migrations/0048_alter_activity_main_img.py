# Generated by Django 4.1.4 on 2023-01-04 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0047_alter_activity_vid_array'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='main_img',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.image'),
        ),
    ]
