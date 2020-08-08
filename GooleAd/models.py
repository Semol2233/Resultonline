from django.db import models




# Google_Ads-web_version
class webGoole_AdsPagename(models.Model):
    PageName         = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.PageName   
# Google-Ads
class web_version(models.Model):
    Ads_page         = models.ForeignKey(webGoole_AdsPagename,on_delete=models.CASCADE,blank= True,null=True)
    Ad_Code          = models.TextField(blank=True)
    Created          = models.DateField(auto_now_add = True)  




# Google_Ads-mobile_version
class mobileGoole_AdsPagename(models.Model):
    PageName         = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.PageName   
# Google-Ads
class mobile_version(models.Model):
    Ads_page         = models.ForeignKey(mobileGoole_AdsPagename,on_delete=models.CASCADE,blank= True,null=True)
    Ad_Code          = models.TextField(blank=True)
    Created          = models.DateField(auto_now_add = True)  
