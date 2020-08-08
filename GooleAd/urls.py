from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from Data_app import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('w/<Ads_page__PageName>', Google_adViewWeb.as_view()),
    path('m/<Ads_page__PageName>', Google_adViewMobile.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
