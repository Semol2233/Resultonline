from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from Blog import views
from Blog.views import PaginatedProjectsAPIView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('', views.Blog_api_root.as_view(), name="home_api"),
    path('filter', views.Blog_api_filter.as_view()),
    # path('blog_home', views.Blog_api_main.as_view()),
    path('cover', views.Blog_api_cover.as_view()),
    path('recommended', views.Blog_api_recomnded.as_view()),  
    path('details/<blog_slug>', views.Blog_api_details.as_view()),
    path('blog_channel/<category>',PaginatedProjectsAPIView.as_view())   


]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
