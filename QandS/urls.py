from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from QandS import views
from .views import *

from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
     path('q_channel/<category>/', PaginatedProjectsAPIView.as_view()),
     path('', qanda_root.as_view())



]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
