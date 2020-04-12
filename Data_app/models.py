from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django.contrib.auth.models import User
from datetime import datetime



class Cetagroy_list(models.Model):
    Channel              = models.CharField(max_length=15)
    Brand_profile        = models.ImageField(upload_to="Brand_Logo",blank=True)
    ChannelDataUrl       = models.CharField(max_length=300, unique=True,blank=True)


    def __str__(self):
        return self.Channel    


class Channel(models.Model):
    channelname       = models.CharField(max_length=20,blank=True)
    channel_profile   = models.ImageField(upload_to="channel_profile",blank=True)
    slug_channel      = models.CharField(max_length=33,blank=False)
   
    
    def __str__(self):
        return self.channelname
    

class PostCreate(models.Model):
    channel            = models.ForeignKey(Channel, on_delete=models.CASCADE)
    title              = models.CharField(max_length = 255)
    slug               = models.CharField(max_length=100,unique=True)
    details            = models.TextField(blank=True)
    mobilebrand        = models.ForeignKey(Cetagroy_list,on_delete=models.CASCADE,null=True,blank=True)
    photo              = models.FileField(upload_to='documents/' ,default='media/channel_profile/1_93A43jqOXZYUr0yFMkcnNw.png')
    tag                = models.CharField(max_length=233,null=True)
    view               = models.IntegerField(blank=True, default=0)
    uploaded           = models.DateTimeField(auto_now_add = True)
    release_date       = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.title
    

class UserProfile(models.Model):
    user              = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    portfolio_link    = models.URLField(blank=True)
    photo             = models.ImageField(upload_to="profile_pic", blank=True)
    
    def __str__(self):
        return self.user.username

class CoverImg(models.Model):
    Cover_img             = models.ImageField(upload_to="Cover_Img", blank=True)
    url                   = models.CharField(null=True, max_length=233)




def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile     = UserProfile.objects.create(user=instance)
post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)

