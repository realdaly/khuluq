# Generated by Django 4.1.4 on 2023-01-08 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0049_production'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='files')),
                ('title', models.CharField(blank=True, max_length=1000)),
            ],
        ),
    ]