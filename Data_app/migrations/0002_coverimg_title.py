# Generated by Django 2.2.5 on 2020-07-21 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coverimg',
            name='title',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
