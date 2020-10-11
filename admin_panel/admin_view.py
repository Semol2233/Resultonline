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
# from .pagination import PaginationHandlerMixin
#end
from django.http import HttpResponse
import random
import datetime
#user model

from GooleAd.models import *
from Data_app.models import *
from admin_panel.admin_api import *


from admin_panel.admin_view import *


#end


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



class admin_view(generics.RetrieveDestroyAPIView):
    # pagination_class       = pagnation
    #permission_classes     = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes     = [permissions.IsAuthenticated]

    queryset = PostCreate.objects.all().order_by('?')
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    serializer_class       = admin_viewseri
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['channel__id','channel__channelname','title','photo','contentowners__authorsname']
    lookup_field           = ('slug')
    # pagination_class       = StandardResultsSetPagination



class admin_view_post(generics.ListCreateAPIView):
    queryset = PostCreate.objects.all().order_by('-id')
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    serializer_class       = admin_viewseri
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['channel__id','channel__channelname','title','photo','contentowners__authorsname']
    # pagination_class       = StandardResultsSetPagination



class catgory_list_admin(generics.ListCreateAPIView):

    queryset               = Cetagroy_list.objects.order_by('-id')
    serializer_class       = BrandProfileInfo
    # pagination_class       = StandadrdResultssSetPdagination





class channel_create(generics.ListCreateAPIView):
    queryset           = Channel.objects.all()
    serializer_class   = UserDettails
    # lookup_field       = ('channelname')


class create_tag_admin(generics.ListCreateAPIView):
    queryset                 = tag_data.objects.all()
    serializer_class         = admin_tagmanager
    filter_backends          = [filters.SearchFilter]
    search_fields            = ['tag_channel_name__channelname']
    # pagination_class         = tag_manager_pagenation


class admin_ownwerCreate(generics.ListCreateAPIView):
    queryset               = Ownercontents.objects.all()
    parser_classes        = (MultiPartParser,FormParser,JSONParser)
    serializer_class       = ContddentOwner





class admin_tagcreators(generics.ListCreateAPIView):
    # pagination_class       = pagnation
    #permission_classes     = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes     = [permissions.IsAuthenticated]

    queryset               = tag_createors.objects.all().order_by('?')
    serializer_class       = tag_data_crators
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['selet_channel__channelname']
    # pagination_class       = Tag_viewr

class hotThisMonth(generics.ListCreateAPIView):
    queryset               = Hot_ThsMonth.objects.all()
    serializer_class       = hotThisMonth_serilaizar



#Cover_Img
class CoverImgs(generics.ListCreateAPIView):
    queryset               = CoverImg.objects.all()[:3]
    serializer_class       = CoverImssge


