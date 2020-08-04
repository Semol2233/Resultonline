from rest_framework import serializers
from Data_app.models import PostCreate,Hot_ThsMonth,UserProfile,Cetagroy_list,Channel,CoverImg,Ownercontents,tag_data,tag_createors
from django.conf import settings
from django.db import models
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.reverse import reverse as api_img
from rest_framework.pagination import PageNumberPagination

#UserAc & User reletet all Data api -> Data relestion  UserDettails
# class UseracAlldata(serializers.ModelSerializer):
#      photo = serializers.SerializerMethodField('get_photo_url')
#      class Meta:
#         model = PostCreate
#         fields = [
#             'id',
#             'title',
#             'photo',
#             'details',
#             'slug',
#             'view',
#             'uploaded',  
#         ]
#      def get_photo_url(self, obj):
#          return obj.photo.url


# #root_content_owner
# class ContensstOwner(serializers.HyperlinkedModelSerializer):
#     List = serializers.SerializerMethodField(read_only=True)
#     class Meta:
#         model = Ownercontents
#         fields = [
#           'id',
#           'authorsname',
#           'authorsprofilrimg',
#           'authorsweblink',
#           'about',
#           'coverImg',
#           'List'
#         ]
#     def get_List(self,obj):
#         qs = obj.postcreate_set.all()[:25]
#         return UseracAlldata(qs,many=True).data




#UserAc & User reletet all Data api -> Api
class UserDettails(serializers.ModelSerializer):
    # Status_list = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Channel
        fields = [
            'id',
            'channelname',
            'channel_profile',
            'is_active'
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
            'slug_channel',
            'is_active'

        ]


class UserPublssicSrtilizer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            'channelname',
            'is_active'

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
            'coverImg',
            'is_active'

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
            'coverImg',
            'is_active'

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
            'ChannelDataUrl',
            'is_active'
            
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
            'is_active'

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
            'is_active'

        ]



class tag_data_crators(serializers.ModelSerializer):
    # Color = serializers.SerializerMethodField()
    class Meta:
        model = tag_createors
        fields = [
            'tag_name',
            'tagSlug',
            'tag_target_link',
            'tagNameBG',
            'is_active'
            
        ]
    # def get_Color(self, object):
    #     data = {
    #             "variant":"primary",
    #             "variant1":"success",
    #             "variant2":"danger",
    #             "variant3":"warning",
    #             "variant4":"info",
    #             "variant5":"dark",
    #             "variant6":"light"
    #             }
    #     return data

        
#root_api
class DRFPostSerializer(serializers.HyperlinkedModelSerializer):
     contentowners   = ContentOwner(read_only=True)
     contentowner = serializers.PrimaryKeyRelatedField(queryset=Ownercontents.objects.all(), source='contentowners' ,write_only=True)

     selete_channel_tag   = tag_data_seri(read_only=True)
     selete_channel_tags = serializers.PrimaryKeyRelatedField(queryset=tag_data.objects.all(), source='selete_channel_tag' ,write_only=True)


     channel         = UserPublicSrtilizer(read_only=True)
     channellist = serializers.PrimaryKeyRelatedField(queryset=Channel.objects.all(), source='channel' ,write_only=True)   

     tag_creator         = tag_data_crators(read_only=True,many=True, required=False)
     tag_creators = serializers.PrimaryKeyRelatedField(queryset=tag_createors.objects.all(), source='tag_creator' ,write_only=True,many=True) 
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
            'selete_channel_tag',
            'selete_channel_tags',
            'id',
            'title',
            'tag_creator',
            'tag_creators',
            'details',
            'SeoTitle',
            'Seoimgalt',
            'SeoMetaDes',
            'photo',
            'mobilebrand',
            'slug',
            'view',
            'release_date',
            'contentlock',
            'contentlenth',
            'contentlink',
            'Persentase',
            'reviewcount',
            'is_active',
            'content_typeModel'

        ]
     def get_target_link(self, object):
        data = {
                "url":"/q&a/api/v1/dtls/",
                "page_name":"Qandq_page_root"
                }
        return data 
    

class dtl_rlt_data(serializers.HyperlinkedModelSerializer):
     contentowners       = ContentOwner(read_only=True)
     channel               = UserPublicSrtilizer(read_only=True)

     class Meta:
        model = PostCreate
        fields = [
            'contentowners',
            'channel',
            'id',
            'title',
            'photo',
            'slug',
            'view',
            'release_date',
            'is_active'

        ]

        




        





#detilsapiview
class DRFPostSdderializer(serializers.HyperlinkedModelSerializer):

     tag_creator     = tag_data_crators(read_only=True,many=True, required=False)
     contentowners   = ContentOwner(read_only=True)
     channel         = UserPublicSrtilizer(read_only=True)
     mobilebrand     = BrandProfileInfo(read_only=True)
     class Meta:
        model = PostCreate
        fields = [
            'channel',
            'contentowners',
            'tag_creator',
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
            'reviewcount',
            'SeoTitle',
            'Seoimgalt',
            'SeoMetaDes',
            'is_active',
            'content_typeModel'

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
            'is_active'
         
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
            'is_active'
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
            'tatag_creatorg',
            'is_active'
          ]
          read_only_fields = ['contentowners']
          read_only_fields = ['channel']



       
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
            'tag_creator',
            'is_active'
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
            'tag_creator',
            'is_active'
        ]
        read_only_fields = ['channel']
        read_only_fields = ['mobilebrand']


class tag_dtlsage_rlt(serializers.ModelSerializer):
    # Color = serializers.SerializerMethodField()
    class Meta:
        model = tag_createors
        fields = [
            'tag_name',
            'is_active'
            
        ]
class recommended_data(serializers.ModelSerializer):
     mobilebrand   = BrandProfileInfo(read_only=True)
     channel       = UserPublicSrtilizer(read_only=True)
     tag_creator   =  tag_dtlsage_rlt(read_only=True,many=True, required=False)

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
            'tag_creator',
            'is_active'
        ]
        read_only_fields = ['channel']
        read_only_fields = ['mobilebrand']




class tagmanager(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            'id',
            'channelname',
            'is_active' 

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
           'is_active'
        ]
        read_only_fields = ['tag_channel_name']
        read_only_fields = ['tag_name']




class tageee_data_crators(serializers.ModelSerializer):
    # Color = serializers.SerializerMethodField()
    class Meta:
        model = tag_createors
        fields = [
            'tag_name',
            'tagSlug',    
            'is_active'  
        ]


class homeTag_page_serializer(serializers.HyperlinkedModelSerializer):
     tag_creator       =  tageee_data_crators(read_only=True)
    #  photo = serializers.SerializerMethodField()
    #  def get_photo(self, obj):
    #     if settings.DEBUG:
    #         host = 'http://localhost:8000'
    #     else:
    #         host = 'http://cdn.resultonlinebd.com/'
    #     return host + obj.photo.url
     class Meta:
        model = PostCreate
        fields = [
            'tag_creator',
            'title',
            'photo',
            'slug',
            'release_date',
            'is_active'
        ]


class Home_tag_serach_page(serializers.HyperlinkedModelSerializer):
     tag_creator         = tag_data_crators(read_only=True,many=True, required=False)
     class Meta:
        model = PostCreate
        fields = [
            'title',
            'tag_creator',
            'photo',
            'release_date',
            'is_active'
        ]





class hot_MonthList(serializers.ModelSerializer):
     contentowner         = ContentOwner(read_only=True)
     tag_creator          = tag_data_crators(read_only=True,many=True, required=False)
     
     class Meta:
        model = PostCreate
        fields = [
            'contentowner',
            'slug',
            'photo',
            'is_active',
            'release_date',
            'tag_creator'

        ]

class hotThisMonth_serilaizar(serializers.HyperlinkedModelSerializer):
     ListMonth    = hot_MonthList(read_only=True,many=True, required=False)
     class Meta:
        model = Hot_ThsMonth
        fields = [
         'ListMonth'
        ]      

    