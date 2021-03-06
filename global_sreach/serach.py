
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
from QandS.models import postmodel_q
from Data_app.models import PostCreate
from Blog.models import postmodel


from django.db.models import Q

#setting option


class qa_pagenation(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class seeearcsssh_filter(APIView, PaginationHandlerMixin):
    pagination_class = qa_pagenation

    def get(self,request,query):
        result = []
        filter_postmodel_q = postmodel_q.objects.filter(Q(title__contains=query) | Q(details__contains=query)).values('title','details','slug','is_active')
        if filter_postmodel_q:
            for p in filter_postmodel_q:
                p['targetUrl'] = {
                    "url": "q&a/api/v1/dtls/",
                    "page_name": "Blog_page"
                }
                result.append(p)
        filter_PostCreate = PostCreate.objects.filter(Q(title__contains=query) | Q(details__contains=query)).values('title','details','photo','slug','is_active','channel__slug_channel')
        if filter_PostCreate:
            for b in filter_PostCreate:
                b['targetUrl'] = {
                    "url": "count/",
                    "page_name": "Blog_page"
                }
                result.append(b)
        filter_postmodel = postmodel.objects.filter(Q(title__contains=query) | Q(details__contains=query)).values('title','details','photo','slug','is_active')
        if filter_postmodel:
            for f in filter_postmodel:
                f['targetUrl'] = {
                    "url": "blog/api/v1/details/",
                    "page_name": "Blog_page"
                }
                result.append(f)
        page = self.paginate_queryset(result)
        paginated_response = self.get_paginated_response(page)
        if len(result) == 0:
            return HttpResponse('No matching data found', status=404)
        return JsonResponse(paginated_response.data, safe=False)




# result['target'] = {'url' : '/blog...'}
# result.append(f)
# result.append(result['target'])
 
# @api_view()
# def searcsssh_filter(request, query):
#         result = []
#         filter_postmodel_q = postmodel_q.objects.filter(Q(title__contains=query) | Q(details__contains=query)).values('title','details','photo')
#         if filter_postmodel_q:
#             for p in filter_postmodel_q:
#              data = {"targetUrl": {
#                     "url":"/q&a/api/v1/dtls/",
#                     "page_name":"q&a"
#                 }}
#              result.append(( p,data))
#         filter_PostCreate = PostCreate.objects.filter(Q(title__contains=query) | Q(details__contains=query)).values('title','details','photo')
#         if filter_PostCreate:
#             for b in filter_PostCreate:
#                 data = {"targetUrl": {     
#                     "url":"/count/",
#                     "page_name":"home_page"
#                 }}
#                 result.append(( b,data))
#         filter_postmodel = postmodel.objects.filter(Q(title__contains=query) | Q(details__contains=query)).values('title','details','photo')
#         if filter_postmodel:
#             for f in filter_postmodel:
#                 data = {"targetUrl": {

#                     "url":"/blog/api/v1/details/",
#                     "page_name":"Blog_page"
#                 }}
#                 result.append(( f,data))
#         return JsonResponse(result, safe=False)