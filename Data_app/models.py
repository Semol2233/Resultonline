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
    is_active         = models.BooleanField(default=True)  
    def __str__(self):
        return self.Channel    


class Channel(models.Model):
    channelname       = models.CharField(max_length=20,blank=True)
    channel_profile   = models.ImageField(upload_to="channel_profile",blank=True)
    slug_channel      = models.CharField(max_length=33,blank=False)
    is_active         = models.BooleanField(default=True)  
    
    def __str__(self):
        return self.channelname




class tag_data(models.Model):
    tag_channel_name  = models.ForeignKey(Channel, on_delete=models.CASCADE)
    tag_name          = models.CharField(max_length=50)
    query_slug        = models.CharField(max_length=50,default="0")
    tag_icon          = models.ImageField(upload_to="tag_icon",blank=False)
    tag_content_link  = models.URLField(max_length=200, blank= True,unique=True)
    is_active         = models.BooleanField(default=True)  
    def __str__(self):
        return str('%s %s' % (self.tag_name,self.tag_channel_name))




class Ownercontents(models.Model):
    authorsname       = models.CharField(max_length=20,blank=True)
    authorsprofilrimg = models.ImageField(upload_to="author_profile" ,blank=True)
    authorsweblink    = models.URLField(max_length = 200)
    about             = models.CharField(max_length = 5000, blank=True,default="hello" )
    coverImg          = models.ImageField(upload_to="author_img",blank=True ,default="author_profile/dasfdad.png")
    is_active         = models.BooleanField(default=True)  
    def __str__(self):
        return self.authorsname 

class tag_createors(models.Model):
    selet_channel      = models.ForeignKey(Channel,on_delete=models.CASCADE,blank= True,null=True)
    tag_name           = models.CharField(max_length=233,null=True)
    tagSlug            = models.SlugField(max_length=233,default="emty")
    tag_target_link    = models.URLField(max_length=100,unique=True,default="0")
    tagNameBG          = models.CharField(max_length=100,default="success")  
    is_active         = models.BooleanField(default=True)  
    def __str__(self):
        return self.tag_name 

class PostCreate(models.Model):
    CHOICES = [
    ('Mobile_Content_type', (
            ('Specfictionrevo', 'r/'),
            ('Review', 's/')
        )
    ),
    ]
    contentowners      = models.ForeignKey(Ownercontents, on_delete=models.CASCADE ,blank=True, null=True)
    channel            = models.ForeignKey(Channel, on_delete=models.CASCADE ,blank=True, null=True)
    title              = models.CharField(max_length = 255)
    slug               = models.CharField(max_length=100,unique=True)
    details            = models.TextField(blank=True)
    selete_channel_tag = models.ForeignKey(tag_data, on_delete=models.CASCADE ,blank=True, null=True)
    mobilebrand        = models.ForeignKey(Cetagroy_list,on_delete=models.CASCADE ,blank=True, null=True )
    photo              = models.FileField(upload_to='documents/' ,default='media/channel_profile/1_93A43jqOXZYUr0yFMkcnNw.png')
    tag_creator        = models.ManyToManyField('tag_createors',default="0") 
    view               = models.IntegerField(blank=True, default=0)
    uploaded           = models.DateTimeField(auto_now_add = True)
    content_typeModel  = models.CharField(max_length=300, choices = CHOICES,default="r/",blank=True)
    release_date       = models.DateField(auto_now_add = True)
    contentlock        = models.BooleanField(default=False)
    contentlenth       = models.IntegerField(default=0, blank=True)
    contentlink        = models.URLField(max_length=200, blank= True , default='http://www.jagobd.com/makkahlive')
    Persentase         = models.IntegerField(blank=True, default= 5)
    reviewcount        = models.IntegerField(blank=True, default= 0)

    SeoTitle          = models.CharField(max_length = 155,blank=True)
    SeoMetaDes        = models.CharField(max_length = 155,blank=True)
    Seoimgalt         = models.CharField(max_length = 255,blank=True)
    is_active         = models.BooleanField(default=True)         




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
    title                 = models.CharField(max_length = 255)

    
    def __str__(self):
        return self.title


class target_link(models.Model):
    target_links = models.CharField(max_length=100)




def userprofile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        userprofile     = UserProfile.objects.create(user=instance)
post_save.connect(userprofile_receiver, sender=settings.AUTH_USER_MODEL)

