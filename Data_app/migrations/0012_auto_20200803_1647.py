# Generated by Django 2.2.5 on 2020-08-03 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_app', '0011_postcreate_content_typemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcreate',
            name='content_typeModel',
            field=models.CharField(blank=True, choices=[('Mobile_Content_type', (('Specfictionrevo', 'r/'), ('Review', 's/')))], default='/r', max_length=300),
        ),
    ]