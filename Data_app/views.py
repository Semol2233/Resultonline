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
from django.http import HttpResponse
#end
from rest_framework.decorators import api_view
import random
import datetime
#user model
import jwt
from Data_app.models import Hot_ThsMonth,PostCreate,UserProfile,UserProfile,Channel,CoverImg,Cetagroy_list,Ownercontents,tag_data,tag_createors
#end
from datetime import datetime, timedelta
#serializer 
from Data_app.api.serializers import (channel_PageTag,ChannelSerializer,
    DRFPostSerializer,Alluser,UserDettails,UserPublicSrtilizer,ClassItemSerializer,BrandPostInfo,BrandProfileInfo,DRFPostSesssrializer,
    latestdata,Releted_Datass,recommended_data,mixPost_serilaizar,ContentOwner,hotThisMonth_serilaizar,ContddentOwner,DRFPostSdderializer,tag_manager_serilizar,tag_data_crators,dtl_rlt_data,homeTag_page_serializer,Home_tag_serach_page )
#end
from Data_app.api.coverimg_api.coverimg import CoverImssge
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from .pagination import PaginationHandlerMixin
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
from rest_framework.settings import api_settings
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


def generate_jwt():
    encoded_jwt = jwt.encode({'key': 'custom_value'}, 'secret', algorithm='HS256').decode('utf-8')
    token = 'Bearer ' + encoded_jwt
    return token

jwt_token = generate_jwt()

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


#Root_Api
class API_objects(generics.ListAPIView):
    # pagination_class       = pagnation
    #permission_classes     = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes     = [permissions.IsAuthenticated]

    queryset = PostCreate.objects.all().order_by('?')
    serializer_class       = DRFPostSerializer
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['channel__channelname','title','details','photo','contentowners__authorsname','selete_channel_tag__query_slug']
    pagination_class       = StandardResultsSetPagination
    
    # print('Token', jwt_token)
    # def get(self, request, *args, **kwargs):
    #     if 'Authorization' in request.headers:
    #         request_header = request.headers['Authorization']
    #     else:
    #         request_header = None
    #     if request_header is not None:
    #         if jwt_token == request_header:
    #             return self.list(request, *args, **kwargs)
    #     return HttpResponse('Authorization header not found', status=400)

#rootupdate
class API_osbjects(generics.RetrieveUpdateDestroyAPIView):
    # pagination_class       = pagnation
    #permission_classes     = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes     = [permissions.IsAuthenticated]

    queryset = PostCreate.objects.all().order_by('?')
    parser_classes = (MultiPartParser,FormParser,JSONParser)
    serializer_class       = DRFPostSdderializer
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['channel__id','channel__channelname','title','photo','contentowners__authorsname']
    lookup_field           = ('slug')
    pagination_class       = StandardResultsSetPagination

    # def put(self, request, *args, **kwargs):
    #     if 'Authorization' in request.headers:
    #         request_header = request.headers['Authorization']
    #     else:
    #         request_header = None
    #     if request_header is not None:
    #         if jwt_token == request_header:
    #             return self.update(request, *args, **kwargs)
    #     return HttpResponse('Authorization header not found', status=400)

    # def patch(self, request, *args, **kwargs):
    #     if 'Authorization' in request.headers:
    #         request_header = request.headers['Authorization']
    #     else:
    #         request_header = None
    #     if request_header is not None:
    #         if jwt_token == request_header:
    #             return self.partial_update(request, *args, **kwargs)
    #     return HttpResponse('Authorization header not found', status=400)

    # def delete(self, request, *args, **kwargs):
    #     if 'Authorization' in request.headers:
    #         request_header = request.headers['Authorization']
    #     else:
    #         request_header = None
    #     if request_header is not None:
    #         if jwt_token == request_header:
    #             return self.destroy(request, *args, **kwargs)
    #     return HttpResponse('Authorization header not found', status=400)


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
    serializer_class       = ChannelSerializer
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
    page_size = 2
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

class UserListView(generics.ListAPIView):
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
    serializer_class       = CoverImssge





class DetailsPageReleteData(generics.ListAPIView):

    queryset               = PostCreate.objects.all().order_by('?')[:2]
    serializer_class       = DRFPostSerializer
    filter_backends        = [filters.SearchFilter]


#example
# class TagDtata(generics.ListAPIView):

#     # queryset = PostCreate.objects.filter(view__startswith=20).filter(release_date__gte=datetime.date(2020,4,2))
#     queryset               = PostCreate.objects.order_by('-id')
#     serializer_class       = DRFPostSerializer
#     lookup_field = ('tag')

class StandadrdResultsSetPdagination(pagination.PageNumberPagination):
    page_size = 3
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
class Brand_ListRendring(generics.ListAPIView):

    queryset               = Cetagroy_list.objects.order_by('?')
    serializer_class       = BrandProfileInfo
    pagination_class       = StandadrdResultssSetPdagination

    # def get(self, request, *args, **kwargs):
    #     if 'Authorization' in request.headers:
    #         request_header = request.headers['Authorization']
    #     else:
    #         request_header = None
    #     if request_header is not None:
    #         if jwt_token == request_header:
    #             return self.list(request, *args, **kwargs)
    #     return HttpResponse('Authorization header not found', status=400)


    # def post(self, request, *args, **kwargs):
    #     if 'Authorization' in request.headers:
    #         request_header = request.headers['Authorization']
    #     else:
    #         request_header = None
    #     if request_header is not None:
    #         if jwt_token == request_header:
    #             return self.create(request, *args, **kwargs)
    #     return HttpResponse('Authorization header not found', status=400)



class StandadsrdResultsSetPdagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100

# class Content_owners(generics.RetrieveAPIView ,generics.ListCreateAPIView,):
#      queryset               = Ownercontents.objects.order_by('-id')
#      serializer_class       = ContensstOwner
#      lookup_field           = ('authorsname')



class Constent_owners(generics.ListAPIView):
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
    queryset               = PostCreate.objects.all().order_by('?')
    serializer_class       = recommended_data
    pagination_class       = recommended_datapagenation
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['channel__slug_channel']




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
    pagination_class       = high_ratetdpagnation


class highss_rsatetd(generics.ListAPIView):
    queryset               = Ownercontents.objects.all()
    serializer_class       = ContentOwner
    parser_classes = (MultiPartParser,FormParser)


class hisghss_rsatetd(generics.RetrieveAPIView):
    queryset               = Ownercontents.objects.all()
    serializer_class       = ContddentOwner
    lookup_field           = ('authorsname')
    parser_classes = (MultiPartParser,FormParser)


#high_ratetd_api
class tag_manager_pagenation(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 4

class tag_mangager(generics.ListAPIView):
    queryset                 = tag_data.objects.all()
    serializer_class         = tag_manager_serilizar
    filter_backends          = [filters.SearchFilter]
    search_fields            = ['tag_channel_name__channelname']
    pagination_class         = tag_manager_pagenation




    
class StandadrdResultsSetPagination(pagination.PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100


#sub_tag_page_Api
# class API_objedfcts(generics.ListCreateAPIView):
    # pagination_class       = pagnation
    #permission_classes     = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes     = [permissions.IsAuthenticated]

    # queryset = PostCreate.objects.all().order_by('-id')
    # serializer_class       = Home_tag_serach_page
    # filter_backends        = [filters.SearchFilter]
    # search_fields          = ['tag_creator__tag_name']
    # pagination_class       = StandadrdResultsSetPagination



class API_objedfcts(APIView, PaginationHandlerMixin):
    pagination_class = StandadrdResultsSetPagination

    def get(self, request, category, *args, **kwargs):
        authors = tag_createors.objects.filter(tagSlug=category).values('tagSlug','tag_name')
        if authors:
            posts = PostCreate.objects.filter(tag_creator__tagSlug=category).values('title', 'slug', 'photo','release_date','view','SeoTitle','SeoMetaDes','Seoimgalt').order_by('-id')
            for author in list(authors):
                response = {
                'tagSlug': author['tagSlug'],
                'tag_name': author['tag_name']

                }
            page = self.paginate_queryset(list(posts))
            response['List'] = page
            paginated_response = self.get_paginated_response(response)
            return JsonResponse(paginated_response.data, safe=False)
        return HttpResponse('No matching data found', status=404)



    
class Tag_viewr(pagination.PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size = 100


#sub_tag_page_Api
class Tag_creatoe_view(generics.ListAPIView):
    # pagination_class       = pagnation
    #permission_classes     = [permissions.IsAuthenticatedOrReadOnly]
    # permission_classes     = [permissions.IsAuthenticated]

    queryset               = tag_createors.objects.all().order_by('?')
    serializer_class       = tag_data_crators
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['selet_channel__channelname']
    pagination_class       = Tag_viewr


    
class Tag_ddviewr(pagination.PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 100

class PaginatedProjectsAPIView(APIView, PaginationHandlerMixin):
    pagination_class = Tag_ddviewr

    def get(self, request, category, *args, **kwargs):
        authors = Ownercontents.objects.filter(authorsname=category).values('authorsname', 'authorsprofilrimg', 'authorsweblink','about','coverImg','page_title','meta_keyword','description')
        if authors:
            posts = PostCreate.objects.filter(contentowners__authorsname=category).values('title', 'slug', 'details', 'photo','view','is_active','channel__slug_channel','SeoTitle','SeoMetaDes','Seoimgalt').order_by('-id')
            for author in list(authors):
                response = {
                'authorsname': author['authorsname'],
                'authorsprofilrimg': author['authorsprofilrimg'],
                'authorsweblink': author['authorsweblink'],
                'page_title': author['page_title'],
                'meta_keyword': author['meta_keyword'],
                'description': author['description'],



                }

                
            page = self.paginate_queryset(list(posts))
            response['List'] = page
            paginated_response = self.get_paginated_response(response)
            return JsonResponse(paginated_response.data, safe=False)
        return HttpResponse('No matching data found', status=404)



    
class Tag_sdcsviewr(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 100


class Reltet_data_datlspage(generics.ListAPIView):
    queryset               = PostCreate.objects.order_by('?')
    serializer_class       = dtl_rlt_data
    filter_backends        = [filters.SearchFilter]
    search_fields          = ['channel__channelname']
    pagination_class       = Tag_sdcsviewr



# class recommended(generics.ListAPIView):
#     queryset               = PostCreate.objects.order_by('?')[8:24]
#     serializer_class       = recommended_data
#     filter_backends        = [filters.SearchFilter]
#     search_fields          = ['channel__id','channel__channelname','title','photo','slug']
#     lookup_field           = ('slug')
#     pagination_class       = recommended_datapagenation



class Tag_page_pagenation(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100

class tag_page(APIView, PaginationHandlerMixin):
    pagination_class = Tag_page_pagenation

    def get(self, request, category, *args, **kwargs):
        authors = tag_createors.objects.filter(tagSlug=category).values('tag_name', 'tagSlug', 'tagNameBG')
        if authors:
            posts = PostCreate.objects.filter(tag_creator__tagSlug=category).values('title', 'slug', 'photo','view','is_active','channel__slug_channel','SeoTitle','SeoMetaDes','Seoimgalt').order_by('-id')
            for author in list(authors):
                response = {
                'tag_name': author['tag_name'],
                'tagSlug': author['tagSlug'],
                'tagNameBG': author['tagNameBG'],
                }
            page = self.paginate_queryset(list(posts))
            response['List'] = page
            paginated_response = self.get_paginated_response(response)
            return JsonResponse(paginated_response.data, safe=False)
        return HttpResponse('No matching data found', status=404)





class Tag_page_pagenation_home(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100

class tag_page_home(APIView, PaginationHandlerMixin):
    pagination_class = Tag_page_pagenation_home

    def get(self, request, category, *args, **kwargs):
        authors = tag_createors.objects.filter(selet_channel__query_slug=category).values('tagSlug', 'tagNameBG','selet_channel__query_slug')
        if authors:
            posts = PostCreate.objects.filter(selete_channel_tag__query_slug=category).values('title', 'slug', 'photo','view','is_active','Seoimgalt').order_by('-id')
            for author in list(authors):
                response = {
                'tagSlug': author['tagSlug'],
                'tagNameBG': author['tagNameBG'],
                'Main_Tag': author['selet_channel__query_slug']

                }
            page = self.paginate_queryset(list(posts))
            response['List'] = page
            paginated_response = self.get_paginated_response(response)
            return JsonResponse(paginated_response.data, safe=False)
        return HttpResponse('No matching data found', status=404)



class channel_sub_data(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100



# class homeTag_page(generics.ListAPIView):
#     queryset               = PostCreate.objects.order_by('-id')
#     serializer_class       = homeTag_page_serializer
#     lookup_field           = ('tag_creator__tag_name')
#     pagination_class       = channel_sub_data


class hotThisMonth(generics.ListAPIView):
    queryset               = Hot_ThsMonth.objects.filter(created_date__gte=datetime.now() - timedelta(days=55))[:4]
    serializer_class       = hotThisMonth_serilaizar




class mix_post(generics.ListAPIView):
    queryset               = PostCreate.objects.filter(channel__slug_channel__contains='Mobile')
    serializer_class       = mixPost_serilaizar


class channelPagepagenation(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100



# class channel_page_Tagdata(generics.RetrieveAPIView):
#     queryset                 = PostCreate.objects.all()
#     serializer_class         = channel_PageTag
#     lookup_field             = ('selete_channel_tag__tag_name')
#     pagination_class         = channelPagepagenation



# class daynamic_channelPage_Subtag(generics.ListAPIView):
#     queryset                 = PostCreate.objects.all().order_by('-id')
#     serializer_class         = channel_PageTag
#     lookup_field             = ('selete_channel_tag__tag_name')
#     pagination_class         = channelPagepagenation

class channel_page_Tagdata(APIView, PaginationHandlerMixin):
    pagination_class = channelPagepagenation

    def get(self, request, category, *args, **kwargs):
        authors = tag_data.objects.filter(query_slug=category).values('tag_name', 'query_slug',)
        if authors:
            posts = PostCreate.objects.filter(selete_channel_tag__query_slug=category).values('title', 'slug','release_date', 'photo','is_active','SeoTitle','SeoMetaDes','Seoimgalt').order_by('-id')
            for author in list(authors):
                response = {
                'tag_name': author['tag_name'],
                'query_slug': author['query_slug']
                }
            page = self.paginate_queryset(list(posts))
            response['List'] = page
            paginated_response = self.get_paginated_response(response)
            return JsonResponse(paginated_response.data, safe=False)
        return HttpResponse('No matching data found', status=404)







class targetData_Value(APIView, PaginationHandlerMixin):
    pagination_class = Tag_page_pagenation_home

    def get(self, request, category, *args, **kwargs):
        authors = tag_createors.objects.filter(tagSlug=category).values('tagSlug', 'tagNameBG','selet_channel__query_slug')
        if authors:
            posts = PostCreate.objects.filter(tag_creator__tagSlug=category).values('title', 'slug', 'photo','view','is_active','Seoimgalt').order_by('-id')
            for author in list(authors):
                response = {
                'tagSlug': author['tagSlug'],
                'tagNameBG': author['tagNameBG'],
                'query_slug': author['selet_channel__query_slug']

                }
            page = self.paginate_queryset(list(posts))
            response['List'] = page
            paginated_response = self.get_paginated_response(response)
            return JsonResponse(paginated_response.data, safe=False)
        return HttpResponse('No matching data found', status=404)





class tag_page_datafimder_pagenation(pagination.PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 100

class listOfdata(APIView, PaginationHandlerMixin):
    pagination_class = tag_page_datafimder_pagenation

    def get(self, request, category, *args, **kwargs):
        authors = tag_createors.objects.filter(selet_channel__query_slug=category).values('selet_channel__query_slug')
        if authors:
            posts = PostCreate.objects.filter(selete_channel_tag__query_slug=category).values('tag_creator__tag_name','tag_creator__tagSlug','tag_creator__tagNameBG').order_by('-id')
            for author in list(authors):
                response = {
                'Main_Tag': author['selet_channel__query_slug']

                }
            page = self.paginate_queryset(list(posts))
            response['List'] = page
            paginated_response = self.get_paginated_response(response)
            return JsonResponse(paginated_response.data, safe=False)
        return HttpResponse('No matching data found', status=404)



@api_view()
def polls_detail(request):
    data = {"data": {
        "Terms": "test",
        "Privacy": "iss",
        "GetinTouch": "test",
        "AboutUs": "test"

    }}
    return JsonResponse(data)