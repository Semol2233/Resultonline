# Generated by Django 2.2.5 on 2020-08-04 13:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Data_app', '0016_hot_thsmonth'),
    ]

    operations = [
        migrations.AddField(
            model_name='hot_thsmonth',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
