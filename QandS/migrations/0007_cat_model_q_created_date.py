# Generated by Django 2.2.5 on 2020-07-19 10:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('QandS', '0006_auto_20200712_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat_model_q',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
