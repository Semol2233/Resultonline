# Generated by Django 2.2.5 on 2020-08-03 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QandS', '0011_auto_20200802_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat_model_q',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='q_shotlist',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]