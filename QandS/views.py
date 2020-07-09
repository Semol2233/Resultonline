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




class qanda_root(generics.ListAPIView):
    queryset               = cat_model_q.objects.all()
    serializer_class       = cat_modelSrtilizer
    paginate_by = 2
    paginate_by_param = 'page_size'
    max_paginate_by = 100
