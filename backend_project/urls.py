
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('simple',include('account_admin_app.urls')),
    path('',include('Data_app.urls')),
    path('adminResultonline/', admin.site.urls),
    path('login',obtain_auth_token,name='token_auth' ),
    path('reg', include('rest_auth.registration.urls')),
    # path('api/login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    
]
