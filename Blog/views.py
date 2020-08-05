from django.shortcuts import render
#rest_framwork
from rest_framework import viewsets
from rest_framework import generics,permissions,mixins,filters
from rest_framework import pagination
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from .pagination import PaginationHandlerMixin
#end

from django.http import HttpResponse
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
    queryset               = cat_model.objects.all()
    serializer_class       = cat_modelSrtilizer
    pagination_class       = StandardResultsSssetPagination


class Blog_api_details(generics.RetrieveAPIView):
    queryset               = postmodel.objects.all()
    serializer_class       = cat_modelSrtilizersss
    lookup_field           = ('slug')

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


class Blog_api_filter(generics.ListAPIView):
    queryset               = postmodel.objects.all()
    serializer_class       = UserPublicSrtilizer_filter
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['catagry_select__cat_slug',]
    pagination_class       = StandardResultsSetPagination

class StandardResssultsSetPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

class Blog_api_main(generics.ListAPIView):
    queryset               = postmodel.objects.all().order_by('-id')[1:11]
    serializer_class       = UserPublicSrtilizer_filter
    pagination_class       = StandardResssultsSetPagination

    
class StandardRessssssultsSetPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100

class Blog_api_cover(generics.ListAPIView):
    queryset               = postmodel.objects.all().order_by('-id')[1:5]
    serializer_class       = UserPublicSrtilizer_filter
    pagination_class       = StandardRessssssultsSetPagination

#[11:15]
class Blog_api_recomnded(generics.ListAPIView):
    queryset               = postmodel.objects.all().order_by('?')[:5]
    serializer_class       = UserPublicSrtilizer_filter






    
class Tag_ddviewr(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100

class PaginatedProjectsAPIView(APIView, PaginationHandlerMixin):
    pagination_class = Tag_ddviewr

    def get(self, request, category, *args, **kwargs):
        authors = cat_model.objects.filter(cat_slug=category).values('cat_name', 'cat_icon', 'cat_description','cat_slug')
        if authors:
            posts = postmodel.objects.filter(catagry_select__cat_slug=category).values('title', 'slug', 'details', 'photo','created_at','view')
            for author in list(authors):
                response = {
                'cat_name': author['cat_name'],
                'cat_icon': author['cat_icon'],
                'cat_description': author['cat_description'],
                'cat_slug': author['cat_slug']

                 }
            page = self.paginate_queryset(list(posts))
            response['List'] = page
            paginated_response = self.get_paginated_response(response)
            return JsonResponse(paginated_response.data, safe=False)
        return HttpResponse('No matching data found', status=404)


class Blog_home_card(generics.ListAPIView):
    queryset               = postmodel.objects.all()[1:3]
    serializer_class       = UserPublicSrtilizer_filter


