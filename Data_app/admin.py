from django.contrib import admin

# Register your models here.
from .models import PostCreate,UserProfile,Cetagroy_list,CoverImg,Channel,Ownercontents,tag_data
admin.site.register(PostCreate)
admin.site.register(UserProfile)
admin.site.register(Cetagroy_list)
admin.site.register(CoverImg)
admin.site.register(Channel)
admin.site.register(Ownercontents)
admin.site.register(tag_data)







