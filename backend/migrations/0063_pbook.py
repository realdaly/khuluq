# Generated by Django 4.1.5 on 2023-01-19 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0062_file_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='pBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=1000)),
                ('author', models.CharField(blank=True, max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
