from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from Accounts.api.views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('login/', obtain_auth_token ,name='login'),
    path('api/token/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'),
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),
    path('register/', registration_view ,name='register'),
    path('logout/', log_out_view ,name='logout'),
    
]
