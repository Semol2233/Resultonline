# Generated by Django 2.2.5 on 2020-07-30 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_app', '0008_auto_20200729_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcreate',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
