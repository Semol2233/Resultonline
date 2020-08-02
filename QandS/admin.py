from django.contrib import admin
from .models import *


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'catagry','awnsr_qna','view','created_at']

admin.site.register(cat_model_q)
admin.site.register(postmodel_q, PostModelAdmin)
admin.site.register(q_shotlist)



