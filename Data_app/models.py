from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django.contrib.auth.models import User
from datetime import datetime



class Cetagroy_list(models.Model):
    Channel           = models.CharField(max_length=15)

    def __str__(self):
        return self.Channel    


class Channel(models.Model):
    channelname = models.CharField(max_length=20,blank=True)
    channel_profile = models.ImageField(upload_to="channel_profile",blank=True)
    slug_channel = models.CharField(max_length=33,blank=False)
    
    def __str__(self):
        return self.channelname
    

class PostCreate(models.Model):
    channel            = models.ForeignKey(Channel, on_delete=models.CASCADE)
    title              = models.CharField(max_length = 255)
    slug               = models.CharField(max_length=100,unique=True)
    details            = models.TextField(blank=True)
    Ceatgory           = models.ForeignKey(Cetagroy_list, related_name='Ceatgory',on_delete=models.CASCADE ,blank=True,null=True)
    photo              = models.FileField(upload_to='documents/')
    view               = models.IntegerField(blank=True,null=True)
    uploaded           = models.DateTimeField(auto_now_add = True)
    release_date       = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.title
    


class ImageField(models.ImageField):
    def value_to_string(self, obj): # obj is Model instance, in this case, obj is 'Class'
        return obj.fig.url # not return self.url



class UserProfile(models.Model):
    user              = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    portfolio_link    = models.URLField(blank=True)
    photo             = models.ImageField(upload_to="profile_pic", blank=True)
    
    def __str__(self):
        return self.user.username



def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile     = UserProfile.objects.create(user=instance)
post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)


# In your models.py add this:
