from django.shortcuts import render
from seo.models import *
from rest_framework.response import Response
from rest_framework.views import APIView

from django.http import JsonResponse
from rest_framework import serializers

from rest_framework import generics
class Seo_PageNameSrtilizer(serializers.ModelSerializer):
    class Meta:
        model = Seo_PageName
        fields = [
            'PageName'
        ]


class Channel_ageName(serializers.ModelSerializer):
    class Meta:
        model = ChannelSeo
        fields = [
            'PageName'
        ]

class HomePage_SeoSrtilizer(serializers.ModelSerializer):
    Page = Seo_PageNameSrtilizer(read_only=True)
    class Meta:
        model = HomePage_Seo
        fields = [
            'Page',
            'page_title',
            'focus_keyword',
            'meta_keyword',
            'description',
            'meta_image',
            'Created'

        ]


class Channel_SeoSrtilizer(serializers.ModelSerializer):
    Channel_Name = Channel_ageName(read_only=True)
    class Meta:
        model = Channel_PageSEO
        fields = [
            'Channel_Name',
            'Channel_title',
            'focus_keyword',
            'meta_keyword',
            'description',
            'meta_image',
            'Created'

        ]

# class SeoHomePage(APIView):
#     def get(self,request):
#         Data = HomePage_Seo.objects.all()
#         serializer = HomePage_SeoSrtilizer(Data, many=True)
#         return Response({"Data": serializer.data})

#     # def post(self, request):
#     #     article = request.data.get('Page')
#     #     serializer = HomePage_SeoSrtilizer(data=article)
#     #     if serializer.is_valid(raise_exception=True):
#     #         article_saved = serializer.save()
#     #     return Response({"success": "Article '{}' created successfully".format(article_saved.title)})



#channel_Api
class SeoHomePage(generics.RetrieveAPIView):
    queryset               = HomePage_Seo.objects.all().order_by('-id')
    serializer_class       = HomePage_SeoSrtilizer
    lookup_field           = ('Page__PageName')


#channel_Api
class SeoChannelPage(generics.RetrieveAPIView):
    queryset               = Channel_PageSEO.objects.all().order_by('-id')
    serializer_class       = Channel_SeoSrtilizer
    lookup_field           = ('Channel_Name__PageName')



