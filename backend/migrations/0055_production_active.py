# Generated by Django 4.1.4 on 2023-01-10 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0054_alter_production_doc_file_alter_production_pdf_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='production',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
