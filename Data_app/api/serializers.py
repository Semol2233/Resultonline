from rest_framework import serializers
from Data_app.models import PostCreate,UserProfile,Cetagroy_list,Channel,CoverImg,Ownercontents
from django.conf import settings
from django.db import models
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.reverse import reverse as api_img
from rest_framework.pagination import PageNumberPagination

#UserAc & User reletet all Data api -> Data relestion  UserDettails
class UseracAlldata(serializers.ModelSerializer):
     photo = serializers.SerializerMethodField('get_photo_url')
     class Meta:
        model = PostCreate
        fields = [
            'id',
            'title',
            'photo',
            'details',
            'slug',
            'view',
            'uploaded',  
        ]
     def get_photo_url(self, obj):
         return obj.photo.url


#root_content_owner
class ContensstOwner(serializers.HyperlinkedModelSerializer):
    List = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Ownercontents
        fields = [
          'id',
          'authorsname',
          'authorsprofilrimg',
          'authorsweblink',
          'about',
          'coverImg',
          'List'
        ]
    def get_List(self,obj):
        qs = obj.postcreate_set.all()[:25]
        return UseracAlldata(qs,many=True).data




#UserAc & User reletet all Data api -> Api
class UserDettails(serializers.ModelSerializer):
    # Status_list = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Channel
        fields = [
            'id',
            'channelname',
            'channel_profile',
            # 'Status_list'
        ]
    # def get_Status_list(self,obj):
    #     qs = obj.postcreate_set.all()
    #     return UseracAlldata(qs,many=True).data
    


    
class UserPublicSrtilizer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            'id',
            'channelname',
            'channel_profile',
            'slug_channel'

        ]

class ContentOwner(serializers.ModelSerializer):
    class Meta:
        model = Ownercontents
        fields = [
            'id',
            'authorsname',
            'authorsprofilrimg',
            'authorsweblink',
            'about',
            'coverImg'

        ]

class ContddentOwner(serializers.ModelSerializer):
    class Meta:
        model = Ownercontents
        fields = [
            'id',
            'authorsname',
            'authorsprofilrimg',
            'authorsweblink',
            'about',
            'coverImg'

        ]
        lookup_field = 'authorsname'




class BrandProfileInfo(serializers.ModelSerializer):
    # ChannelDataUrl      = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Cetagroy_list
        fields = [
            'id',
            'Channel',
            'Brand_profile',
            'ChannelDataUrl'
            
        ]
#root_api
class DRFPostSerializer(serializers.HyperlinkedModelSerializer):
     contentowners   = ContentOwner(read_only=True)
     contentowner = serializers.PrimaryKeyRelatedField(queryset=Ownercontents.objects.all(), source='contentowners' ,write_only=True)

     channel         = UserPublicSrtilizer(read_only=True)
     channellist = serializers.PrimaryKeyRelatedField(queryset=Channel.objects.all(), source='channel' ,write_only=True)   

     mobilebrand     = BrandProfileInfo(read_only=True)
     mobilebarand = serializers.PrimaryKeyRelatedField(queryset=Cetagroy_list.objects.all(), source='mobilebrand' ,write_only=True)

     class Meta:
        model = PostCreate
        fields = [
            'contentowners',
            'channel',
            'contentowner',
            'channellist',
            'mobilebarand',
            'id',
            'title',
            'details',
            'photo',
            'mobilebrand',
            'slug',
            'view',
            'release_date',
            'tag',
            'contentlock',
            'contentlenth',
            'contentlink',
            'Persentase',
            'reviewcount'

        ]

        

    
#detilsapiview
class DRFPostSdderializer(serializers.HyperlinkedModelSerializer):
     contentowners   = ContentOwner(read_only=True)
     channel         = UserPublicSrtilizer(read_only=True)
     mobilebrand     = BrandProfileInfo(read_only=True)
     class Meta:
        model = PostCreate
        fields = [
            'channel',
            'contentowners',
            'id',
            'title',
            'details',
            'photo',
            'mobilebrand',
            'slug',
            'view',
            'release_date',
            'tag',
            'contentlock',
            'contentlenth',
            'contentlink',
            'Persentase',
            'reviewcount'

        ]
        lookup_field = 'slug'
        read_only_fields = ['details','Persentase','title','slug','tag','photo','contentlenth','contentlock','contentlink']
        




class latestdata(serializers.HyperlinkedModelSerializer):
      
     contentowners   = ContentOwner(read_only=True)
     channel         = UserPublicSrtilizer(read_only=True)
     mobilebrand     = serializers.CharField()

     class Meta:
        model = PostCreate
        fields = [
            'contentowners',
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
        read_only_fields = ['contentowners']
        read_only_fields = ['channel']






class DRFPostSesssrializer(serializers.HyperlinkedModelSerializer):
     contentowners   = ContentOwner(read_only=True)
     channel         = UserPublicSrtilizer(read_only=True)
     mobilebrand     = serializers.CharField()

     class Meta:
        model = PostCreate
        fields = [
            'contentowners',
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
        read_only_fields = ['contentowners']
        read_only_fields = ['channel']



class Alluser(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('portfolio_link','photo')


# -------------------------
class ClassItemSerializer(serializers.HyperlinkedModelSerializer):
      contentowners   = ContentOwner(read_only=True)
      channel   = UserPublicSrtilizer(read_only=True)
      mobilebrand  = serializers.CharField()

      class Meta:
          model = PostCreate
          fields = [
            'contentowners',
            'channel',
            'id',
            'title',
            'details',
            'photo',
            'mobilebrand',
            'slug',
            'view',
            'uploaded',
            'release_date',
            'contentlock',
            'contentlenth',
            'contentlink',
            'Persentase',
            'tag'
          ]
          read_only_fields = ['contentowners']
          read_only_fields = ['channel']

class CoverImge(serializers.ModelSerializer):
      class Meta:
          model = CoverImg
          fields = [
            'id',
            'Cover_img',
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


class Releted_Datass(serializers.ModelSerializer):
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



class recommended_data(serializers.ModelSerializer):
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