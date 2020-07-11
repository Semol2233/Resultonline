from rest_framework import serializers
from QandS.models import *
from django.conf import settings
from django.db import models
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()



class UserPublicSrtilizer(serializers.ModelSerializer):
    class Meta:
        model = postmodel_q
        fields = [
            'id',
            'qname',
            'q_slug',
            'catagry_select',
            'decribe_post',
            'post_img',
            'post_views',
            'created_at'
        ]


class cat_modelSrtilizer(serializers.HyperlinkedModelSerializer):
    List = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = cat_model_q
        fields = [
            'id',
            'q_name',
            'q_icon',
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
            'shot_list_data'
        ]


class qna_dlts_api(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = cat_model_q
        fields = [
            'id',
            'q_name',
            'q_icon',
            'q_slug',
        
        ]




class dtls_api_qna(serializers.ModelSerializer):
    catagry_select = qna_dlts_api(read_only=True)
    class Meta:
        model = postmodel_q
        fields = [
            'id',
            'qname',
            'q_slug',
            'catagry_select',
            'awnsr_qna',
            'decribe_post',
            'post_img',
            'post_views'

        ]

        lookup_field = 'q_slug'
        read_only_fields = ['qname','q_slug','catagry_select','awnsr_qna','decribe_post','post_img']