from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from Blog import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.Blog_api_root.as_view(), name="home_api"),
    path('api/v1/filter', views.Blog_api_filter.as_view()),



    
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
