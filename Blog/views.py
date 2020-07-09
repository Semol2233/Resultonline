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
    paginate_by = 2
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class Blog_api_details(generics.RetrieveAPIView):
    queryset               = postmodel.objects.all()
    serializer_class       = cat_modelSrtilizersss
    lookup_field           = ('blog_slug')

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



class Blog_api_main(generics.ListAPIView):
    queryset               = postmodel.objects.all().order_by('-id')[6:11]
    serializer_class       = UserPublicSrtilizer_filter

    

class Blog_api_cover(generics.ListAPIView):
    queryset               = postmodel.objects.all().order_by('-id')[1:5]
    serializer_class       = UserPublicSrtilizer_filter


class Blog_api_recomnded(generics.ListAPIView):
    queryset               = postmodel.objects.all().order_by('?')[11:15]
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
            posts = postmodel.objects.filter(catagry_select__cat_slug=category).values('title', 'blog_slug', 'decribe_post', 'post_img','created_at')
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