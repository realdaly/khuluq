# Generated by Django 4.1.4 on 2023-01-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0039_alter_activity_main_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid_id', models.CharField(max_length=5000)),
                ('title', models.CharField(max_length=1000)),
            ],
        ),
    ]
