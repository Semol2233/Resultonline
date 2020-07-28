from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from Data_app import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)


urlpatterns = [
    path('', views.API_objects.as_view(), name="home_api"),
    path('users',views.Alluserprofile.as_view(),name='user'),
    path('facebook/', views.FacebookLogin.as_view(), name='fb_login'),
    path('socialaccounts/',SocialAccountListView.as_view(),name='social_account_list'),
    path('update/<int:pk>/',views.update_objects.as_view()),
    path('channels/<channelname>/',views.UserListView.as_view()),
    path('ChannelDataList',views.ChannelDataList.as_view()),
    path('user/',views.UserList.as_view()),
    path('details/<slug>',views.ServiceDetailAPIView.as_view()),
    path('channeldel',views.Channel_Data.as_view()),
    path('TopContent',views.RandomDtata.as_view()),
    path('Coverimgapi',views.CoverImgs.as_view()),
    path('detailspageR',views.DetailsPageReleteData.as_view()),
    path('trending',views.TrendingPost.as_view()),
    # path('tsssssag/<tag>',views.TagDtata.as_view()),
    path('Brand',views.Brand_InfoDtata.as_view()),
    path('listBrand',views.Brand_ListRendring.as_view()),
    # path('channel/<authorsname>',views.Content_owners.as_view()),
    path('extra',views.Constent_owners.as_view()),
    path('latestdata',views.Latest_data.as_view()),
    path('Releted_Data',views.Releted_Data.as_view()),
    
    path('recommended_data',views.recommended.as_view()),
    path('channel_Dataapi',views.channel_Dataapi.as_view()),
    path('high_ratetd',views.high_ratetd.as_view()),
    path('posslink',views.highss_rsatetd.as_view()),
    path('hi/<authorsname>/',views.hisghss_rsatetd.as_view()),


    path('count/<slug>',views.API_osbjects.as_view()),
    path('tagmanager',views.tag_mangager.as_view()),

    path('sub_tag_manager',views.API_objedfcts.as_view()),#delete_some_issue
    path('Tag_creator',views.Tag_creatoe_view.as_view()),
    
    path('channel/<category>', PaginatedProjectsAPIView.as_view()),

    path('dtl_rlt', Reltet_data_datlspage.as_view()),
    path('tagPage/<category>/', tag_page.as_view()),
    path('tagPage_home/<category>/', tag_page_home.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
