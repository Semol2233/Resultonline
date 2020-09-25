from django.urls import path
from .views import Login,home
urlpatterns = [
    path('',Login),
    path('home/',home,name="home")
]
