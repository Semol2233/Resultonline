from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from Data_app import views
from django.conf.urls.static import static
from django.conf import settings
from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)


urlpatterns = [
    path('', views.API_objects.as_view(), name="home_api"),
    path('img/<int:pk>/', views.Quteapiview.as_view()),
    path('users',views.Alluserprofile.as_view(),name='user'),
    path('facebook/', views.FacebookLogin.as_view(), name='fb_login'),
    path('socialaccounts/',SocialAccountListView.as_view(),name='social_account_list'),
    path('update/<int:pk>/',views.update_objects.as_view()),
    path('channel/<channelname>/',views.UserListView.as_view()),
    path('ChannelDataList',views.ChannelDataList.as_view()),
    path('user/',views.UserList.as_view()),
    path('details/<slug>',views.ServiceDetailAPIView.as_view()),
    path('channeldel',views.Channel_Data.as_view()),
    path('TopContent',views.RandomDtata.as_view()),
    path('Coverimgapi',views.CoverImgs.as_view()),
    path('detailspageR',views.DetailsPageReleteData.as_view()),
    path('trending',views.TrendingPost.as_view()),
    path('Tag/<Tag>',views.TagDtata.as_view()),
    path('Brand',views.Brand_InfoDtata.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
