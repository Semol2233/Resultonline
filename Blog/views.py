from django.shortcuts import render
#rest_framwork
from rest_framework import viewsets
from rest_framework import generics,permissions,mixins,filters
from rest_framework import pagination
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser

#end
import random
import datetime
#user model
from Blog.models import *
#end

#serializer 
from Blog.api.serializers import *
#end

#setting option
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
#end

# DJango built in login 
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,get_user_model,login,logout
# end

#social Auth 
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
# end

#user filter
from django.contrib.auth import get_user_model
User = get_user_model()
#end

#list view -> APi
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser


class StandardResultsSssetPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100
    

#root
class Blog_api_root(generics.ListAPIView):
    queryset               = cat_model.objects.all().order_by('-id')
    serializer_class       = cat_modelSrtilizer
    pagination_class       = StandardResultsSssetPagination



class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class Blog_api_filter(generics.ListAPIView):
    queryset               = postmodel.objects.all().order_by('-id')
    serializer_class       = UserPublicSrtilizer_filter
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['catagry_select__cat_name']
    pagination_class       = StandardResultsSetPagination



class Blog_api_main(generics.ListAPIView):
    queryset               = postmodel.objects.all().order_by('-id')[6:11]
    serializer_class       = UserPublicSrtilizer_filter

    

class Blog_api_cover(generics.ListAPIView):
    queryset               = postmodel.objects.all().order_by('-id')[1:5]
    serializer_class       = UserPublicSrtilizer_filter

    