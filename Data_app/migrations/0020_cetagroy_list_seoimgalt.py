# Generated by Django 2.2.5 on 2020-08-25 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Data_app', '0019_auto_20200821_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='cetagroy_list',
            name='Seoimgalt',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
