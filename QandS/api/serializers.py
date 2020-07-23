from rest_framework import serializers
from QandS.models import *
from django.conf import settings
from django.db import models
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()



class UserPublicSrtilizer(serializers.ModelSerializer):
    # post_img = serializers.SerializerMethodField()
    # def get_post_img(self, obj):
    #     if settings.DEBUG:
    #         host = 'http://localhost:8000'
    #     else:
    #         host = 'https://example.com'
    #     return host + obj.post_img.url
    # target_link = serializers.SerializerMethodField()
    class Meta:
        model = postmodel_q
        fields = [
            'id',
            'title',
            'slug',
            'catagry',
            'details',
            'photo',
            'view',
            'created_at',
            # 'target_link'
        ]

    # def get_target_link(self, object):
    #     data = {"target_url": {
    #             "url":"/q&a/api/v1/dtls/",
    #             "page_name":"Qandq_page_root"
    #             }}
    #     return data 

        
class cat_modelSrtilizer(serializers.HyperlinkedModelSerializer):
    List = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = cat_model_q
        fields = [
            'id',
            'publisher',
            'q_icon',
            'q_slug',
            'List',
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
            'shot_list_data'
        ]


class qna_dlts_api(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cat_model_q
        fields = [
            'id',
            'publisher',
            'q_icon',
            'q_slug',
        
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
            'photo',
            'view'

        ]

        lookup_field = 'slug'
        read_only_fields = ['title','slug','catagry','awnsr_qna','details','photo']