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




class UserPublicSrtilizer(serializers.ModelSerializer):
    class Meta:
        model = postmodel
        fields = [
            'id',
            'title',
            'slug',
            'details',
            'photo',
            'view',
            'created_at',
            'is_active',
            'SeoTitle',
            'SeoMetaDes',
            'Seoimgalt'
        ]


class cat_modelSrtilizer(serializers.HyperlinkedModelSerializer):
    List = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = cat_model
        fields = [
            'id',
            'cat_name',
            'cat_description',
            'cat_full_data',
            'cat_icon',
            'cat_slug',
            'List',
            'is_active',
            'SeoTitle',
            'SeoMetaDes',
            'Seoimgalt'
        ]


    def get_List(self,obj):
        qs = obj.postmodel_set.all()[:3]
        return UserPublicSrtilizer(qs,many=True).data


class cat_model_releson(serializers.ModelSerializer):

    class Meta:
        model = cat_model
        fields = [
            'id',
            'cat_name',
            'is_active'
    
        ]


class cat_modelSrtilizersss(serializers.ModelSerializer):
    catagry_select         = cat_model_releson(read_only=True)
    class Meta:
        model = postmodel
        fields = [
            'id',
            'title',
            'slug',
            'catagry_select',
            'details',
            'photo',
            'view',
            'is_active',
            'SeoTitle',
            'SeoMetaDes',
            'Seoimgalt'         
    
        ]
        lookup_field = 'slug'

#filter_data

class cat_modelSrtilizer_filter(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = cat_model
        fields = [
            'id',
            'cat_name',
            'cat_icon',
            'cat_slug',
            'is_active'
            'SeoTitle',
            'SeoMetaDes',
            'Seoimgalt'
        ]



class UserPublicSrtilizer_filter(serializers.ModelSerializer):
    catagry_select  =  cat_modelSrtilizer_filter(read_only=True)
    class Meta:
        model = postmodel
        fields = [
            'id',
            'title',
            'slug',
            'details',
            'photo',
            'catagry_select',
            'view',
            'created_at'
            # 'is_active',
            # 'SeoTitle',
            # 'SeoMetaDes',
            # 'Seoimgalt'
        ]












