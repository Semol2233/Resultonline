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
from Data_app.models import PostCreate,UserProfile,UserProfile,Channel,CoverImg,Cetagroy_list,Ownercontents
#end

#serializer 
from Data_app.api.serializers import (
    DRFPostSerializer,Alluser,UserDettails,UserPublicSrtilizer,UseracAlldata,ClassItemSerializer,
    UseracAlldata,CoverImge,BrandPostInfo,BrandProfileInfo,ContensstOwner,DRFPostSesssrializer,
    latestdata,Releted_Datass,recommended_data,ContentOwner,ContddentOwner,DRFPostSdderializer
    )
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


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 13
    page_size_query_param = 'page_size'
    max_page_size = 100


#Root_Api
class API_objects(generics.ListCreateAPIView):
    # pagination_class       = pagnation
    #permission_classes     = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes     = [permissions.IsAuthenticated]

    queryset = PostCreate.objects.all().order_by('?')
    serializer_class       = DRFPostSerializer
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['channel__id','channel__channelname','title','photo','tag','contentowners__authorsname']
    pagination_class       = StandardResultsSetPagination
#rootupdate
class API_osbjects(generics.RetrieveUpdateDestroyAPIView):
    # pagination_class       = pagnation
    #permission_classes     = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes     = [permissions.IsAuthenticated]

    queryset = PostCreate.objects.all().order_by('?')
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    serializer_class       = DRFPostSdderializer
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['channel__id','channel__channelname','title','photo','tag','contentowners__authorsname']
    lookup_field           = ('slug')
    pagination_class       = StandardResultsSetPagination


class channel_Data(pagination.PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 100


#channel_Api
class channel_Dataapi(generics.ListAPIView):
    # pagination_class       = pagnation
    #permission_classes     = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes     = [permissions.IsAuthenticated]
    queryset               = PostCreate.objects.all().order_by('-id')
    serializer_class       = DRFPostSerializer
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['channel__slug_channel']
    pagination_class       = channel_Data




#Latest_Api
class Latest_data(generics.ListAPIView):
    # pagination_class       = pagnation
    #permission_classes     = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes     = [permissions.IsAuthenticated]

    queryset               = PostCreate.objects.all().order_by('-id')[:5]
    serializer_class       = latestdata
    # filter_backends        = [filters.SearchFilter]
    # search_fields          = ['channel__id','channel__channelname','title','photo','tag','contentowners__authorsname']
    # pagination_class       = StandardResultsSetPagination


class StandadrdResultsSetPdagfination(pagination.PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 100

#channel data query
class Channel_Data(generics.ListAPIView):
    # pagination_class       = pagnation
    permission_classes     = [permissions.IsAuthenticatedOrReadOnly]
    queryset               = PostCreate.objects.all().order_by('-id')
    serializer_class       = DRFPostSerializer
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['channel__slug_channel']
    pagination_class       = StandadrdResultsSetPdagfination


#update view -> Api
class update_objects(
      generics.RetrieveAPIView,
      mixins.UpdateModelMixin,
      mixins.DestroyModelMixin
    ):

    permission_classes     = []
    authentication_classes = []
    queryset           = PostCreate.objects.all()
    serializer_class   = DRFPostSerializer

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self,request,*args, **kwargs):
        return self.destroy(request,*args, **kwargs)


#extra generic update -> APi
class Quteapiview(
    generics.RetrieveUpdateDestroyAPIView
    ):

    permission_classes     = []
    authentication_classes = []
    queryset               = PostCreate.objects.all()
    serializer_class       = DRFPostSerializer



class Alluserprofile(generics.ListAPIView):
    permission_classes     = []
    authentication_classes = []
    queryset               = UserProfile.objects.all()
    serializer_class       = Alluser
    
    
class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter


class ChannelDataList(generics.ListAPIView):
    queryset               = PostCreate.objects.all()
    serializer_class       = DRFPostSerializer
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['channel__id','channel__channelname','title','photo','slug','Mobile_Brand']
    lookup_field = ('slug')



# class UserListView(generics.RetrieveAPIView):
#     queryset           = User.objects.filter(is_active=True)
#     serializer_class   = UserDettails
#     lookup_field       = 'username'

class UserListView(generics.RetrieveAPIView,generics.ListCreateAPIView):
    queryset           = Channel.objects.all()
    serializer_class   = UserDettails
    lookup_field       = ('channelname')





class UserList(generics.ListAPIView):
    queryset               = User.objects.all()
    serializer_class       = UserPublicSrtilizer



# class CarView(generics.ListAPIView):

#     def get(self, request, *args, **kwargs):
#         queryset = Channel.objects.all()
#         serializer = UseracAlldata(queryset, many=True, context={"request":request})
#         return Response(serializer.data, status=status.HTTP_200_OK)



class ServiceDetailAPIView(generics.RetrieveAPIView):
    queryset = PostCreate.objects.all()
    serializer_class = ClassItemSerializer
    lookup_field = ('slug')


class StandardResultsSetPdagination(pagination.PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 100


#Top_Data
class RandomDtata(generics.ListAPIView):

    # queryset = PostCreate.objects.filter(view__startswith=20).filter(release_date__gte=datetime.date(2020,4,2))
    queryset               = PostCreate.objects.order_by('-view')
    serializer_class       = DRFPostSerializer
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['channel__id','channel__channelname','title','photo','slug']
    lookup_field           = ('slug')
    pagination_class       = StandardResultsSetPdagination


#Trending_Api
class TrendingPost(generics.ListAPIView):
    data = '2020-01-01'
    queryset               = PostCreate.objects.order_by('-view').filter(release_date__gte=data).filter(release_date__iso_year__gte=2005)
    serializer_class       = DRFPostSerializer



#Cover_Img
class CoverImgs(generics.ListAPIView):
    queryset               = CoverImg.objects.all()[:3]
    serializer_class       = CoverImge





class DetailsPageReleteData(generics.ListAPIView):

    queryset               = PostCreate.objects.all().order_by('?')[:2]
    serializer_class       = DRFPostSerializer
    filter_backends        = [filters.SearchFilter]


#example
class TagDtata(generics.ListAPIView):

    # queryset = PostCreate.objects.filter(view__startswith=20).filter(release_date__gte=datetime.date(2020,4,2))
    queryset               = PostCreate.objects.order_by('-id')
    serializer_class       = DRFPostSerializer
    lookup_field = ('tag')

class StandadrdResultsSetPdagination(pagination.PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 100

class Brand_InfoDtata(generics.ListAPIView):

    # queryset = PostCreate.objects.filter(view__startswith=20).filter(release_date__gte=datetime.date(2020,4,2))
    queryset               = PostCreate.objects.order_by('-id').filter(channel__slug_channel='Mobile-Phone')
    serializer_class       = BrandPostInfo
    pagination_class       = StandadrdResultsSetPdagination
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['mobilebrand__Channel']



class StandadrdResultssSetPdagination(pagination.PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 100
#Brand_ListRendring
class Brand_ListRendring(generics.ListCreateAPIView,):

    queryset               = Cetagroy_list.objects.order_by('?')
    serializer_class       = BrandProfileInfo
    pagination_class       = StandadrdResultssSetPdagination

class StandadsrdResultsSetPdagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100

class Content_owners(generics.RetrieveAPIView ,generics.ListCreateAPIView,):
     queryset               = Ownercontents.objects.order_by('-id')
     serializer_class       = ContensstOwner
     lookup_field           = ('authorsname')



class Constent_owners(generics.ListAPIView ,generics.ListCreateAPIView,):
     queryset               = PostCreate.objects.order_by('-id')
     serializer_class       = DRFPostSesssrializer
     filter_backends        = [filters.SearchFilter]
     search_fields          = ['contentowners__authorsname']

    
#Brand_ListRendring
class Releted_Data(generics.ListAPIView):
    queryset               = PostCreate.objects.all().order_by('?')[3:7]
    serializer_class       = Releted_Datass
    
#recommended_api
class recommended_datapagenation(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4

#recommended_api
class recommended(generics.ListAPIView):
    queryset               = PostCreate.objects.order_by('?')[8:24]
    serializer_class       = recommended_data
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['channel__id','channel__channelname','title','photo','slug']
    lookup_field           = ('slug')
    pagination_class       = recommended_datapagenation

#high_ratetd_api
class high_ratetdpagnation(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 4

#high_ratetd_api
class high_ratetd(generics.ListAPIView):
    queryset               = PostCreate.objects.order_by('-view')
    serializer_class       = recommended_data
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['channel__id','channel__channelname','title','photo','slug']
    lookup_field           = ('slug')
    pagination_class       = recommended_datapagenation


class highss_rsatetd(generics.ListAPIView ,generics.ListCreateAPIView,):
    queryset               = Ownercontents.objects.all()
    serializer_class       = ContentOwner
    parser_classes = (MultiPartParser,FormParser)


class hisghss_rsatetd(generics.RetrieveUpdateDestroyAPIView):
    queryset               = Ownercontents.objects.all()
    serializer_class       = ContddentOwner
    lookup_field           = ('authorsname')
    parser_classes = (MultiPartParser,FormParser)








    