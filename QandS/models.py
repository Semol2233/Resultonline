from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
from PIL import Image

class cat_model_q(models.Model):
    publisher        = models.CharField(max_length=50)
    q_icon        = models.ImageField(upload_to='Blog_cat_icon/')
    q_slug        = models.SlugField(max_length=50)
    created_date   = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.publisher

class postmodel_q(models.Model):
    title              = models.CharField(max_length=255)
    slug             = models.SlugField(max_length=255,unique=True)
    catagry            = models.ForeignKey(cat_model_q,on_delete=models.CASCADE,blank=True)
    awnsr_qna          = models.TextField(blank=True)
    details       = models.TextField(blank=True)
    photo           = models.ImageField(upload_to='media_blog/')
    view         = models.IntegerField(blank=True, default= 0)
    created_at         = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title





class q_shotlist(models.Model):
    shot_list_name   = models.CharField(max_length=255)
    shot_list_data   = models.URLField(max_length=200, blank= True , default='emty')


    def __str__(self):
        return self.shot_list_name

