# Generated by Django 2.2.5 on 2020-05-04 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_app', '0005_auto_20200504_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownercontents',
            name='about',
            field=models.CharField(blank=True, default='hello', max_length=5000),
        ),
    ]