# Generated by Django 2.2.5 on 2020-07-23 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QandS', '0007_cat_model_q_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postmodel_q',
            old_name='decribe_post',
            new_name='details',
        ),
        migrations.RenameField(
            model_name='postmodel_q',
            old_name='q_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='postmodel_q',
            old_name='qname',
            new_name='title',
        ),
    ]
