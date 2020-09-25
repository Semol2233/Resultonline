from django.contrib import admin

# Register your models here.
from .models import PostCreate,Hot_ThsMonth,UserProfile,Cetagroy_list,CoverImg,Channel,Ownercontents,tag_data,tag_createors
admin.site.register(PostCreate)
admin.site.register(UserProfile)
admin.site.register(Cetagroy_list)
admin.site.register(CoverImg)
admin.site.register(Channel)
admin.site.register(Ownercontents)
admin.site.register(tag_data)
admin.site.register(tag_createors) 
admin.site.register(Hot_ThsMonth) 









