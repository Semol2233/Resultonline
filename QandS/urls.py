from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from QandS import views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    # path('', views.Blog_api_root.as_view(), name="home_api"),  


]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
