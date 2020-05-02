from rest_framework import serializers
from Data_app.models import PostCreate,UserProfile,Cetagroy_list,Channel,CoverImg
from django.conf import settings
from django.db import models
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.reverse import reverse as api_img


#UserAc & User reletet all Data api -> Data relestion  UserDettails
class UseracAlldata(serializers.ModelSerializer):
     mobilebrand  = serializers.CharField()
     class Meta:
        model = PostCreate
        fields = [
            'id',
            'title',
            'photo',
            'mobilebrand',
            'details',
            'slug',
            'view',
            'uploaded',  
        ]



#UserAc & User reletet all Data api -> Api
class UserDettails(serializers.ModelSerializer):
    Status_list = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Channel
        fields = [
            'id',
            'channelname',
            'channel_profile',
            'Status_list'
        ]
    def get_Status_list(self,obj):
        qs = obj.postcreate_set.all()
        return UseracAlldata(qs,many=True).data
    


    
class UserPublicSrtilizer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            'id',
            'channelname',
            'channel_profile',
            'slug_channel'

        ]

# class ContentOwner(serializers.ModelSerializer):
#     class Meta:
#         model = Ownercdontents
#         fields = [
#             'id',
#             'authorsname',
#             'authorsprofilrimg',
#             'authorsweblink'

#         ]

#root_api
class DRFPostSerializer(serializers.HyperlinkedModelSerializer):
      
   
     channel         = UserPublicSrtilizer(read_only=True)
     mobilebrand     = serializers.CharField()

     class Meta:
        model = PostCreate
        fields = [
  
            'channel',
            'id',
            'title',
            'details',
            'photo',
            'mobilebrand',
            'slug',
            'view',
            'release_date',
            'tag'
        ]
      
        read_only_fields = ['channel']




class Alluser(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('portfolio_link','photo')






# -------------------------
class ClassItemSerializer(serializers.HyperlinkedModelSerializer):
      channel   = UserPublicSrtilizer(read_only=True)
      mobilebrand  = serializers.CharField()

      class Meta:
          model = PostCreate
          fields = [
            'channel',
            'id',
            'title',
            'details',
            'photo',
            'mobilebrand',
            'slug',
            'view',
            'uploaded',
            'release_date'
          ]
          read_only_fields = ['channel']

class CoverImge(serializers.ModelSerializer):
      class Meta:
          model = CoverImg
          fields = [
            'id',
            'Cover_img',
          ]
    









class BrandProfileInfo(serializers.ModelSerializer):
    # ChannelDataUrl      = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Cetagroy_list
        fields = [
            'id',
            'Channel',
            'Brand_profile',
            'ChannelDataUrl',
            

        ]
       
    # def get_ChannelDataUrl(self,obj):
    #     data = 'http://127.0.0.1:8000/dd?search=' 
    #     return "{data}+{Channel}".format(Channel=obj.Channel)


class BrandPostInfo(serializers.ModelSerializer):
     mobilebrand   = BrandProfileInfo(read_only=True)
     channel       = UserPublicSrtilizer(read_only=True)

     class Meta:
        model = PostCreate
        fields = [
            'channel',
            'mobilebrand',
            'id',
            'title',
            'details',
            'photo',
            'slug',
            'view',
            'release_date',
            'tag'
        ]
        read_only_fields = ['channel']
        read_only_fields = ['mobilebrand']


