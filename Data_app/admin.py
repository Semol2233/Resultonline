from django.contrib import admin

# Register your models here.
from .models import PostCreate,UserProfile,Cetagroy_list,Channel
admin.site.register(PostCreate)
admin.site.register(UserProfile)
admin.site.register(Cetagroy_list)
admin.site.register(Channel)


