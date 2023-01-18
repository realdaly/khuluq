# Generated by Django 4.1.5 on 2023-01-16 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0057_alter_activity_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='audio',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='backend.audio'),
        ),
    ]
