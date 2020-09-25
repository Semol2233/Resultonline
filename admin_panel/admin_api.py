from rest_framework import serializers
from Blog.models import *
from django.conf import settings
from django.db import models
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.reverse import reverse as api_img
from rest_framework.pagination import PageNumberPagination

from Data_app.models import *
# from Data_app.api.serializers import *







class ContentOwner(serializers.ModelSerializer):
    class Meta:
        model = Ownercontents
        fields = [
            'id',
            'authorsname',
            'authorsprofilrimg',
            'authorsweblink',
            'about',
            'coverImg',
            'is_active'

        ]

class UserPublssicSrtilizer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            'channelname',
            'is_active'

        ]
        
class tag_data_seri(serializers.ModelSerializer):
    tag_channel_name         = UserPublssicSrtilizer(read_only=True)
    class Meta:
        model = tag_data
        fields = [
            'id',
            'tag_name',
            'tag_icon',
            'query_slug',
            'tag_content_link',
            'tag_channel_name',
            'is_active'

        ]



class UserPublicSrtilizer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            'id',
            'channelname',
            'channel_profile',
            'slug_channel',
            'is_active'

        ]



class tag_data_crators(serializers.ModelSerializer):
    # Color = serializers.SerializerMethodField()
    class Meta:
        model = tag_createors
        fields = [
            'tag_name',
            'tagSlug',
            'tag_target_link',
            'tagNameBG',
            'is_active'
            
        ]



class BrandProfileInfo(serializers.ModelSerializer):
    # ChannelDataUrl      = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Cetagroy_list
        fields = [
            'id',
            'Channel',
            'Brand_profile',
            'ChannelDataUrl',
            'Seoimgalt',
            'is_active'
            
        ]

#root_api
class admin_viewseri(serializers.HyperlinkedModelSerializer):
     contentowners   = ContentOwner(read_only=True)
     contentowner = serializers.PrimaryKeyRelatedField(queryset=Ownercontents.objects.all(), source='contentowners' ,write_only=True)

     selete_channel_tag   = tag_data_seri(read_only=True)
     selete_channel_tags = serializers.PrimaryKeyRelatedField(queryset=tag_data.objects.all(), source='selete_channel_tag' ,write_only=True)


     channel         = UserPublicSrtilizer(read_only=True)
     channellist = serializers.PrimaryKeyRelatedField(queryset=Channel.objects.all(), source='channel' ,write_only=True)   

     tag_creator         = tag_data_crators(read_only=True,many=True, required=False)
     tag_creators = serializers.PrimaryKeyRelatedField(queryset=tag_createors.objects.all(), source='tag_creator' ,write_only=True,many=True) 
     mobilebrand     = BrandProfileInfo(read_only=True)
     mobilebarand = serializers.PrimaryKeyRelatedField(queryset=Cetagroy_list.objects.all(), source='mobilebrand' ,write_only=True,required=False)

     class Meta:
        model = PostCreate
        fields = [
            'contentowners',
            'channel',
            'contentowner',
            'channellist',
            'mobilebarand',
            'selete_channel_tag',
            'selete_channel_tags',
            'id',
            'title',
            'tag_creator',
            'tag_creators',
            'details',
            'SeoTitle',
            'Seoimgalt',
            'SeoMetaDes',
            'photo',
            'mobilebrand',
            'slug',
            'view',
            'release_date',
            'contentlock',
            'contentlenth',
            'contentlink',
            'Persentase',
            'reviewcount',
            'is_active',
            'content_typeModel'

        ]
     def get_target_link(self, object):
        data = {
                "url":"/q&a/api/v1/dtls/",
                "page_name":"Qandq_page_root"
                }
        return data 
    





#UserAc & User reletet all Data api -> Api
class UserDettails(serializers.ModelSerializer):
    # Status_list = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Channel
        fields = [
            'id',
            'channelname',
            'channel_profile',
            'is_active'
            # 'Status_list'
        ]



class tagmanahhger(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            'id',
            'channelname',
            'is_active' 
        ]


class admin_tagmanager(serializers.HyperlinkedModelSerializer):
     tag_channel_name   = tagmanahhger(read_only=True)
     tag_channel_names = serializers.PrimaryKeyRelatedField(queryset=Channel.objects.all(), source='tag_channel_name' ,write_only=True,required=False)

     class Meta:
        model = tag_data
        fields = [
           'tag_name',
           'tag_icon',
           'query_slug',
           'tag_content_link',
           'tag_channel_name',
           'tag_channel_names',
           'is_active'
        ]
        # read_only_fields = ['tag_channel_name']
        # read_only_fields = ['tag_name']



class ContddentOwner(serializers.ModelSerializer):
    class Meta:
        model = Ownercontents
        fields = [
            'id',
            'authorsname',
            'authorsprofilrimg',
            'authorsweblink',
            'about',
            'coverImg',
            'is_active',
            'page_title',
            'focus_keyword',
            'meta_keyword',
            'description',
            'Created'
        ]




class tagmanahhgsser(serializers.ModelSerializer):
    class Meta:
        model = tag_data
        fields = [
            'id',
            'tag_channel_name',
            'is_active' 
        ]




class tag_data_crators(serializers.HyperlinkedModelSerializer):
    selet_channel   = tagmanahhgsser(read_only=True)
    selet_channels = serializers.PrimaryKeyRelatedField(queryset=tag_data.objects.all(), source='selet_channel' ,write_only=True)
    class Meta:
        model = tag_createors
        fields = [
            'selet_channel',
            'selet_channels',
            'tag_name',
            'tagSlug',
            'tag_target_link',
            'tagNameBG',
            'is_active'
            
        ]



class hotMonlistingthList(serializers.ModelSerializer):
     tag_creator          = tag_data_crators(read_only=True,many=True, required=False)  
     class Meta:
        model = PostCreate
        fields = [
            'title',
            'slug',
            'photo',
            'is_active',
            'release_date',
            'tag_creator',
            'SeoTitle',
            'SeoMetaDes',
            'Seoimgalt'
        ]      


class hotThisMonth_serilaizar(serializers.ModelSerializer):
     ListMonth    = hotMonlistingthList(read_only=True,many=True, required=False)
     ListMonths   = serializers.PrimaryKeyRelatedField(queryset=PostCreate.objects.all(), source='ListMonth' ,write_only=True,many=True)
     class Meta:
        model = Hot_ThsMonth
        fields = [
         'ListMonth',
         'ListMonths'
        ]  




    #  tag_creator         = tag_data_crators(read_only=True,many=True, required=False)
    #  tag_creators = serializers.PrimaryKeyRelatedField(queryset=tag_createors.objects.all(), source='tag_creator' ,write_only=True,many=True) 




class UseracAlldata(serializers.ModelSerializer):
     class Meta:
        model = target_link
        fields = [
            'target_links'
        ]


class CoverImssge(serializers.ModelSerializer):
      # target_link = serializers.SerializerMethodField("get_display")
      class Meta:
          model = CoverImg
          fields = [
            'title',
            'Cover_img',
            'url'
          ]
      # def get_display(self, obj):
      #   return "/count/"
