# Generated by Django 2.2.5 on 2020-08-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0005_postmodel_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat_model',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
