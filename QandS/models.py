from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django.contrib.auth.models import User
from datetime import datetime



class cat_model(models.Model):
    q_name        = models.CharField(max_length=50)
    q_icon        = models.ImageField(upload_to='Blog_cat_icon/')
    q_slug        = models.SlugField(max_length=50)

    def __str__(self):
        return self.cat_name

class postmodel(models.Model):
    qname              = models.CharField(max_length=255)
    q_slug          = models.SlugField(max_length=255,unique=True)
    catagry_select     = models.ForeignKey(cat_model,on_delete=models.CASCADE,blank=True)
    decribe_post       = models.TextField(blank=True)
    post_img           = models.ImageField(upload_to='media_blog/')
    post_views         = models.IntegerField(blank=True, default= 0)
    created_at         = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title
    
