# Generated by Django 2.2.5 on 2020-08-07 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0002_auto_20200807_1112'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage_seo',
            old_name='PageName',
            new_name='Page',
        ),
    ]