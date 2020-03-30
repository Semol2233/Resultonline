from django.shortcuts import render
#rest_framwork
from rest_framework import viewsets
from rest_framework import generics,permissions,mixins,filters,pagination
from rest_framework import authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser
#end


#user model
from Data_app.models import PostCreate,UserProfile,UserProfile,Channel
#end

#serializer 
from Data_app.api.serializers import (
    DRFPostSerializer,Alluser,UserDettails,UserPublicSrtilizer,UseracAlldata,ClassItemSerializer,
    UseracAlldata
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


class API_objects(
    generics.ListAPIView
    ):
    # pagination_class       = pagnation
    #parser_classes = [JSONParser]
    permission_classes     = [permissions.IsAuthenticatedOrReadOnly]
    queryset               = PostCreate.objects.all()
    serializer_class       = DRFPostSerializer
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['channel__id','channel__channelname','title','photo']


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
    search_fields          = ['channel__id','channel__channelname','title','photo','slug']
    lookup_field = ('slug')



# class UserListView(generics.RetrieveAPIView):
#     queryset           = User.objects.filter(is_active=True)
#     serializer_class   = UserDettails
#     lookup_field       = 'username'

class UserListView(generics.RetrieveAPIView):
    queryset           = Channel.objects.all()
    serializer_class   = UserDettails
    lookup_field       = ('channelname')





class UserList(generics.ListAPIView):
    queryset               = User.objects.all()
    serializer_class       = UserPublicSrtilizer



class CarView(generics.ListAPIView):

    def get(self, request, *args, **kwargs):
        queryset = Channel.objects.all()
        serializer = UseracAlldata(queryset, many=True, context={"request":request})
        return Response(serializer.data, status=status.HTTP_200_OK)



# ---------------------



class ServiceDetailAPIView(generics.RetrieveAPIView):
    queryset = PostCreate.objects.all()
    serializer_class = ClassItemSerializer
    lookup_field = ('slug')



    
