# Generated by Django 4.1.4 on 2022-12-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_activity_options_alter_activity_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='created_at',
            field=models.DateField(),
        ),
    ]