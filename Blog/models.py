from django.db.models.signals import post_save
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.shortcuts import reverse
from django.contrib.auth.models import User
from datetime import datetime



class cat_model(models.Model):
    cat_name        = models.CharField(max_length=50)
    cat_full_data   = models.URLField(max_length=200,blank= True,default="No link")
    cat_icon        = models.ImageField(upload_to='Blog_cat_icon/')
    cat_description = models.CharField(max_length=50, default="No data")
    cat_slug        = models.SlugField(max_length=50)
    is_active          = models.BooleanField(default=True)    
    def __str__(self):
        return self.cat_name

class postmodel(models.Model):
    title              = models.CharField(max_length=255)
    slug               = models.SlugField(max_length=255,unique=True)
    catagry_select     = models.ForeignKey(cat_model,on_delete=models.CASCADE,blank=True)
    details            = models.TextField(blank=True)
    photo              = models.ImageField(upload_to='media_blog/')
    view               = models.IntegerField(blank=True, default= 0)
    created_at         = models.DateTimeField(auto_now_add=True)
    is_active          = models.BooleanField(default=True)         




    def __str__(self):
        return self.title
    
