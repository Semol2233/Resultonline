# Generated by Django 2.2.5 on 2020-07-23 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_cat_model_cat_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel',
            old_name='decribe_post',
            new_name='details',
        ),
        migrations.RenameField(
            model_name='postmodel',
            old_name='blog_slug',
            new_name='slug',
        ),
    ]
