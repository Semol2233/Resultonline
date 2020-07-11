from django.contrib import admin
from .models import *


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['qname', 'q_slug', 'catagry_select', 'post_img','post_views','created_at']

admin.site.register(cat_model_q)
admin.site.register(postmodel_q, PostModelAdmin)
admin.site.register(q_shotlist)



