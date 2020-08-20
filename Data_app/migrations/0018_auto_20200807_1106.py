# Generated by Django 2.2.5 on 2020-08-07 11:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Data_app', '0017_hot_thsmonth_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ownercontents',
            name='Created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ownercontents',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='ownercontents',
            name='focus_keyword',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='ownercontents',
            name='meta_keyword',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='ownercontents',
            name='page_title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]