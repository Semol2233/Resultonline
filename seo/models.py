from django.db import models

# Create your models here.

class Seo_PageName(models.Model):
    PageName         = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.PageName   

class HomePage_Seo(models.Model):
    Page             = models.ForeignKey(Seo_PageName,on_delete=models.CASCADE,blank= True,null=True)
    page_title       = models.CharField(max_length=200,blank=True)
    focus_keyword    = models.CharField(max_length=200,blank=True)
    meta_keyword     = models.CharField(max_length=200,blank=True)
    description      = models.TextField(blank=True)
    meta_image       = models.ImageField(upload_to="seo_img" ,blank=True)
    Created          = models.DateField(auto_now_add = True)  

    def __str__(self):
        return self.page_title  


class ChannelSeo(models.Model):
    PageName         = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.PageName 


class Channel_PageSEO(models.Model):
    Channel_Name     = models.ForeignKey(ChannelSeo,on_delete=models.CASCADE,blank= True,null=True)
    Channel_title    = models.CharField(max_length=200,blank=True)
    focus_keyword    = models.CharField(max_length=200,blank=True)
    meta_keyword     = models.CharField(max_length=200,blank=True)
    description      = models.TextField(blank=True)
    meta_image       = models.ImageField(upload_to="seo_img" ,blank=True)
    Created          = models.DateField(auto_now_add = True)  
    def __str__(self):
        return self.Channel_title  



