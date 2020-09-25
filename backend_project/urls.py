
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
#from rest_framework_simplejwt import views as jwt_views
from global_sreach.serach import seeearcsssh_filter
from resize_image.resizeimage import image_filter
from admin_panel.admin_view import *

urlpatterns = [
    path('simple',include('account_admin_app.urls')),
    path('',include('Data_app.urls')),
    path('blog/api/v1/',include('Blog.urls')),
    path('q&a/api/v1/',include('QandS.urls')),
    path('s/',include('seo.urls')),
    path('ad/',include('GooleAd.urls')),


    path('admin/', admin.site.urls),
    path('login/',obtain_auth_token,name='token_auth' ),
    path('reg/', include('rest_auth.registration.urls')),
    #path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    #path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('s/<query>/', searcsssh_filter),
    path('filter_image/<img>/<int:height>/<int:width>/', image_filter),
    path('serach/<query>/', seeearcsssh_filter.as_view()),
    # admin_area
    path('createpost', admin_view_post.as_view()),
    path('updateview/<slug>/', admin_view.as_view()),
    path('create_catagory', catgory_list_admin.as_view()),
    path('createchannel', channel_create.as_view()),
    path('createtag', create_tag_admin.as_view()),
    path('createOwner', admin_ownwerCreate.as_view()),
    path('createtagcreators', admin_tagcreators.as_view()),
    path('create_hotproduct', hotThisMonth.as_view()),

    



    




]
