from rest_framework import serializers
from QandS.models import *
from django.conf import settings
from django.db import models
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()



# return img full reuest url-------------------->
    # post_img = serializers.SerializerMethodField()
    # def get_post_img(self, obj):
    #     if settings.DEBUG:
    #         host = 'http://localhost:8000'
    #     else:
    #         host = 'https://example.com'
    #     return host + obj.post_img.url

#add some extra data------------->
    # target_link = serializers.SerializerMethodField()
    # def get_target_link(self, object):
    #     data = {"target_url": {
    #             "url":"/q&a/api/v1/dtls/",
    #             "page_name":"Qandq_page_root"
    #             }}
    #     return data 

    #rename model feild name serilaizar --------------->
    #    location = serializers.CharField(source='viewd')+
    #            'location'

    # def viewd(self):
    #     return self.view

class UserPublicSrtilizer(serializers.ModelSerializer):
    target_link = serializers.SerializerMethodField()
    class Meta:
        model = postmodel_q
        fields = [
            'id',
            'title',
            'slug',
            'catagry',
            'details',
            'view',
            'created_at',
            'is_active',
            'target_link'
        ]

    def get_target_link(self, object):
        data = {
                "url":"/q&a/api/v1/dtls/",
                "page_name":"Qandq_page_root"
                }
        return data 
        
class cat_modelSrtilizer(serializers.HyperlinkedModelSerializer):
    List = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = cat_model_q
        fields = [
            'id',
            'publisher',
            'is_active',
            'q_slug',
            'List'
        ]

    def get_List(self,obj):
        qs = obj.postmodel_q_set.all()[:3]
        return UserPublicSrtilizer(qs,many=True).data






class q_shot_list_data(serializers.ModelSerializer):
    class Meta:
        model = q_shotlist
        fields = [
            'id',
            'shot_list_name',
            'shot_list_data',
            'is_active'
        ]


class qna_dlts_api(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cat_model_q
        fields = [
            'id',
            'publisher',
            'q_slug',
            'is_active'
        
        ]




class dtls_api_qna(serializers.ModelSerializer):
    catagry = qna_dlts_api(read_only=True)
    class Meta:
        model = postmodel_q
        fields = [
            'id',
            'title',
            'slug',
            'catagry',
            'awnsr_qna',
            'details',
            'view',
            'is_active'

        ]

        lookup_field = 'slug'
        read_only_fields = ['title','slug','catagry','awnsr_qna','details']



class qna_fast_check(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cat_model_q
        fields = [
            'id',
            'publisher',
            'is_active'
        ]


class qanda_fast_check(serializers.ModelSerializer):
    catagry = qna_fast_check(read_only=True)
    class Meta:
        model = postmodel_q
        fields = [
            'title',
            'slug',
            'view',
            'catagry',
            'is_active'

        ]

        lookup_field = 'slug'
        read_only_fields = ['title','slug','catagry','is_active']