
from django.shortcuts import render,get_object_or_404
#rest_framwork


from rest_framework import pagination

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser,FormParser,MultiPartParser
from django.http import HttpResponse ,HttpResponseNotFound
#end

from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
import jwt


from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from QandS.pagination import PaginationHandlerMixin
from QandS.models import *
from Data_app.models import *
from Blog.models import *




#setting option


class qa_pagenation(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class searcsssh_filter(APIView, PaginationHandlerMixin):
    pagination_class = qa_pagenation

    def get(self,request,query,*args, **kwargs):
        result = []
        filter_post = postmodel_q.objects.filter(qname__icontains=query).values()
        if filter_post:
            for p in filter_post:
               result.append(p)
        filter_post = PostCreate.objects.filter(title__icontains=query).values()
        if filter_post:
            for p in filter_post:
               result.append(p)
        filter_post = postmodel.objects.filter(title__icontains=query).values()
        if filter_post:
            for p in filter_post:
               result.append(p)
            page = self.paginate_queryset(result)
            result = page
            paginated_response = self.get_paginated_response(result)
            return JsonResponse(paginated_response.data, safe=False)
        return HttpResponse('No matching data found', status=404)