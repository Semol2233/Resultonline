from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from GooleAd.models import *
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import JsonResponse
from rest_framework import serializers

from rest_framework import generics
class webGoole_AdsPagenames(serializers.ModelSerializer):
    class Meta:
        model = webGoole_AdsPagename
        fields = [
            'PageName'
        ]


class mobileGoole_AdsPagenames(serializers.ModelSerializer):
    class Meta:
        model = mobileGoole_AdsPagename
        fields = [
            'PageName'
        ]

class Google_adsWeb(serializers.ModelSerializer):
    Ads_page = webGoole_AdsPagenames(read_only=True)
    class Meta:
        model = web_version
        fields = [
            'Ads_page',
            'Ad_Code',
            'Created'
        ]

class Google_adsMobbile(serializers.ModelSerializer):
    Ads_page = mobileGoole_AdsPagenames(read_only=True)
    class Meta:
        model = mobile_version
        fields = [
            'Ads_page',
            'Ad_Code',
            'Created'
        ]

class Google_adViewWeb(generics.RetrieveAPIView):
    queryset               = web_version.objects.all().order_by('-id')
    serializer_class       = Google_adsWeb
    lookup_field           = ('Ads_page__PageName')



class Google_adViewMobile(generics.RetrieveAPIView):
    queryset               = mobile_version.objects.all().order_by('-id')
    serializer_class       = Google_adsMobbile
    lookup_field           = ('Ads_page__PageName')



mylist = [23,5,3,2,5,]
mylist[2:]
print(mylist)
