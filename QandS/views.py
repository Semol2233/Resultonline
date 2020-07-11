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
import jwt
from .filters import  DynamicSearchFilter
import random
import datetime
#user model
from .models import *
#serializer 
from QandS.api.serializers import *
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from .pagination import PaginationHandlerMixin
#setting option
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
#end




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

# class qa_pagenation(pagination.PageNumberPagination):
#     page_size = 2
#     page_size_query_param = 'page_size'
#     max_page_size = 100


# class PaginatedProjectsAPIView(APIView, PaginationHandlerMixin):
#     pagination_class = qa_pagenation

#     def get(self, request, category, *args, **kwargs):
#         request_header = request.headers['Authorization']
#         if jwt_token == request_header:
#             authors = cat_model_q.objects.filter(q_slug=category).values('q_name', 'q_icon', 'q_slug')
#             if authors:
#                 posts = postmodel_q.objects.filter(catagry_select__q_slug=category).values('qname', 'q_slug', 'decribe_post', 'post_img','post_views')
#                 for author in list(authors):
#                     response = {
#                     'q_name': author['q_name'],
#                     'q_icon': author['q_icon'],
#                     'q_slug': author['q_slug']
#                      }
#                 page = self.paginate_queryset(list(posts))
#                 response['List'] = page
#                 paginated_response = self.get_paginated_response(response)
#                 return JsonResponse(paginated_response.data, safe=False)
#             return HttpResponse('No matching data found', status=404)
#         return HttpResponse('Authorization header not found', status=400)



class qa_pagenation(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100


class PaginatedProjectsAPIView(APIView, PaginationHandlerMixin):
    pagination_class = qa_pagenation

    def get(self, request, category, *args, **kwargs):
        authors = cat_model_q.objects.filter(q_slug=category).values('q_name', 'q_icon', 'q_slug')
        if authors:
            posts = postmodel_q.objects.filter(catagry_select__q_slug=category).values('qname', 'q_slug', 'decribe_post', 'post_img','post_views')
            for author in list(authors):
                response = {
                    'q_name': author['q_name'],
                    'q_icon': author['q_icon'],
                    'q_slug': author['q_slug']
                }
            page = self.paginate_queryset(list(posts))
            response['List'] = page
            paginated_response = self.get_paginated_response(response)
            return JsonResponse(paginated_response.data, safe=False)
        return HttpResponse('No matching data found', status=404)

# class qanda_rssoot(generics.ListAPIView):
#     queryset               = cat_model_q.objects.all()
#     serializer_class       = cat_modelSrtilizer
#     pagination_class       = qa_pagenasssstion



# class qanda_root(APIView):
#     pagination_class = PageNumberPagination
#     print('Token', jwt_token)
#     def get(self, request, format=None,*args, **kwargs):
#         request_header = request.headers['Authorization']
#         if jwt_token == request_header:
#             snippets = cat_model_q.objects.all()
#             serializer = cat_modelSrtilizer(snippets, many=True)
#             return Response(serializer.data)
#         return HttpResponse('Authorization header not found', status=400)




class qa_pagenasssstion(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 100

class qanda_root(generics.ListAPIView):
    queryset               = cat_model_q.objects.all()
    serializer_class       = cat_modelSrtilizer
    pagination_class       = qa_pagenasssstion



class q_shotlist_data(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class channel_Dataapi(generics.ListAPIView):
    queryset               = q_shotlist.objects.all().order_by('?')
    serializer_class       = q_shot_list_data
    pagination_class       = q_shotlist_data





# class dtls_api_qna_view(generics.RetrieveUpdateDestroyAPIView):

#     queryset = postmodel_q.objects.all()
#     serializer_class       = dtls_api_qna
#     lookup_field           = ('q_slug')


class dtls_api_qna_view(generics.RetrieveAPIView,mixins.UpdateModelMixin):

    queryset = postmodel_q.objects.all()
    serializer_class       = dtls_api_qna
    lookup_field           = ('q_slug')

    def put(self,request,*args, **kwargs):
        return self.update(request,*args, **kwargs)

