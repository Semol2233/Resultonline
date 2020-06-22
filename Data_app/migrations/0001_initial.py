# Generated by Django 2.2.5 on 2020-06-22 16:03

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
            name='Ownercontents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorsname', models.CharField(blank=True, max_length=20)),
                ('authorsprofilrimg', models.ImageField(blank=True, upload_to='author_profile')),
                ('authorsweblink', models.URLField()),
                ('about', models.CharField(blank=True, default='hello', max_length=5000)),
                ('coverImg', models.ImageField(blank=True, default='author_profile/dasfdad.png', upload_to='author_img')),
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
            name='tag_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
                ('query_slug', models.CharField(default='0', max_length=50)),
                ('tag_icon', models.ImageField(upload_to='tag_icon')),
                ('tag_content_link', models.URLField(blank=True, unique=True)),
                ('tag_channel_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Data_app.Channel')),
            ],
        ),
        migrations.CreateModel(
            name='tag_createors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=233, null=True)),
                ('tag_target_link', models.URLField(default='0', max_length=100, unique=True)),
                ('main_tag_select', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Data_app.tag_data')),
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
                ('view', models.IntegerField(blank=True, default=0)),
                ('uploaded', models.DateTimeField(auto_now_add=True)),
                ('release_date', models.DateField(auto_now_add=True)),
                ('contentlock', models.BooleanField(default=False)),
                ('contentlenth', models.IntegerField(blank=True, default=0)),
                ('contentlink', models.URLField(blank=True, default='http://www.jagobd.com/makkahlive')),
                ('Persentase', models.IntegerField(blank=True, default=5)),
                ('reviewcount', models.IntegerField(blank=True, default=0)),
                ('channel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Data_app.Channel')),
                ('contentowners', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Data_app.Ownercontents')),
                ('mobilebrand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Data_app.Cetagroy_list')),
                ('selete_channel_tag', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Data_app.tag_data')),
                ('tag_creator', models.ManyToManyField(default='0', to='Data_app.tag_createors')),
            ],
        ),
    ]
