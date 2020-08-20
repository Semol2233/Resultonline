# Generated by Django 2.2.5 on 2020-08-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel_PageSEO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Channel_Name', models.CharField(blank=True, max_length=200)),
                ('Channel_title', models.CharField(blank=True, max_length=200)),
                ('focus_keyword', models.CharField(blank=True, max_length=200)),
                ('meta_keyword', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('meta_image', models.ImageField(blank=True, upload_to='seo_img')),
                ('Created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomePage_Seo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PageName', models.CharField(blank=True, max_length=200)),
                ('page_title', models.CharField(blank=True, max_length=200)),
                ('focus_keyword', models.CharField(blank=True, max_length=200)),
                ('meta_keyword', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('meta_image', models.ImageField(blank=True, upload_to='seo_img')),
                ('Created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]