from rest_framework import serializers
from Data_app.models import PostCreate,UserProfile,Cetagroy_list,Channel,CoverImg,Ownercontents,tag_data,tag_createors
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


class UserPublssicSrtilizer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            'channelname',

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



class tag_data_seri(serializers.ModelSerializer):
    tag_channel_name         = UserPublssicSrtilizer(read_only=True)
    class Meta:
        model = tag_data
        fields = [
            'id',
            'tag_name',
            'tag_icon',
            'query_slug',
            'tag_content_link',
            'tag_channel_name',

        ]
class tag_dddata_seri(serializers.ModelSerializer):
    tag_channel_name         = UserPublssicSrtilizer(read_only=True)
    class Meta:
        model = tag_data
        fields = [
            'id',
            'tag_name',
            'tag_icon',
            'query_slug',
            'tag_content_link',
            'tag_channel_name',

        ]



class tag_data_crators(serializers.ModelSerializer):
    selet_channel   = UserPublssicSrtilizer(read_only=True)
    class Meta:
        model = tag_createors
        fields = [
            'selet_channel',
            'tag_target_link',
            'tag_name'
        ]


        
#root_api
class DRFPostSerializer(serializers.HyperlinkedModelSerializer):
     contentowners   = ContentOwner(read_only=True)
     contentowner = serializers.PrimaryKeyRelatedField(queryset=Ownercontents.objects.all(), source='contentowners' ,write_only=True)

    #  selete_channel_tag   = tag_data_seri(read_only=True)
    #  selete_channel_tags = serializers.PrimaryKeyRelatedField(queryset=tag_data.objects.all(), source='selete_channel_tag' ,write_only=True)


     channel         = UserPublicSrtilizer(read_only=True)
     channellist = serializers.PrimaryKeyRelatedField(queryset=Channel.objects.all(), source='channel' ,write_only=True)   

    #  tag_creator         = tag_data_crators(read_only=True,many=True, required=False)
    #  tag_creators = serializers.PrimaryKeyRelatedField(queryset=tag_createors.objects.all(), source='tag_creator' ,write_only=True,many=True) 

     mobilebrand     = BrandProfileInfo(read_only=True)
     mobilebarand = serializers.PrimaryKeyRelatedField(queryset=Cetagroy_list.objects.all(), source='mobilebrand' ,write_only=True,required=False)

     class Meta:
        model = PostCreate
        fields = [
            'contentowners',
            'channel',
            'contentowner',
            'channellist',
            'mobilebarand',
            # 'selete_channel_tag',
            # 'selete_channel_tags',
            'id',
            'title',
            # 'tag_creator',
            # 'tag_creators',
            'details',
            'photo',
            'mobilebrand',
            'slug',
            'view',
            'release_date',
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
            'contentlock',
            'contentlenth',
            'contentlink',
            'Persentase',
            'reviewcount'

        ]
        lookup_field = 'slug'
        read_only_fields = ['details','Persentase','title','slug','tag_creator','photo','contentlenth','contentlock','contentlink']
        




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
            'tag_creator'
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
            'tatag_creatorg'
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
            'tag_creator'
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
            'tag_creator'
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
            'tag_creator'
        ]
        read_only_fields = ['channel']
        read_only_fields = ['mobilebrand']




class tagmanager(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            'id',
            'channelname',    

        ]

       

class tag_manager_serilizar(serializers.ModelSerializer):

     tag_channel_name       = tagmanager(read_only=True)
     
     
     class Meta:
        model = tag_data
        fields = [
           'tag_name',
           'tag_icon',
           'query_slug',
           'tag_content_link',
           'tag_channel_name',
        ]
        read_only_fields = ['tag_channel_name']
        read_only_fields = ['tag_name']


