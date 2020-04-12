# Generated by Django 2.2.5 on 2020-04-12 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cetagroy_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Channel', models.CharField(max_length=15)),
                ('Brand_profile', models.ImageField(blank=True, upload_to='Brand_Logo')),
                ('ChannelDataUrl', models.CharField(blank=True, max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channelname', models.CharField(blank=True, max_length=20)),
                ('channel_profile', models.ImageField(blank=True, upload_to='channel_profile')),
                ('slug_channel', models.CharField(max_length=33)),
            ],
        ),
        migrations.CreateModel(
            name='CoverImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cover_img', models.ImageField(blank=True, upload_to='Cover_Img')),
                ('url', models.CharField(max_length=233, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_link', models.URLField(blank=True)),
                ('photo', models.ImageField(blank=True, upload_to='profile_pic')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostCreate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('details', models.TextField(blank=True)),
                ('photo', models.FileField(default='media/channel_profile/1_93A43jqOXZYUr0yFMkcnNw.png', upload_to='documents/')),
                ('tag', models.CharField(max_length=233, null=True)),
                ('view', models.IntegerField(blank=True, default=0)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('release_date', models.DateField(auto_now_add=True)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data_app.Channel')),
                ('mobilebrand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Data_app.Cetagroy_list')),
            ],
        ),
    ]
