# Generated by Django 4.1.4 on 2023-01-07 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0048_alter_activity_main_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField(max_length=5000)),
                ('main_img', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='backend.image')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
