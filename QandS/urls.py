from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from QandS import views
from .views import *
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
     path('', qanda_root.as_view()),
     path('channel/<category>', PaginatedProjectsAPIView.as_view()),
     path('short_list', channel_Dataapi.as_view()),
     path('dtls/<slug>', dtls_api_qna_view.as_view()),
     path('q_related_data/<catagry__publisher>', dtls_apwi_qna_view.as_view()),
     path('qanda_home', qanda_home_card.as_view()),
     path('data_filter_shot_list', qanda_shotlist_data_filter.as_view()),




]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
