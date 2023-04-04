from django.urls import path
from user.views import RegisterView, LoginView
from rest_framework_simplejwt.views import (TokenObtainPairView, 
                                            TokenRefreshView, 
                                            TokenVerifyView)
# route for user account creation

urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('create-token/', TokenObtainPairView.as_view(), name='create-user'),
    path('refresh-token/', TokenRefreshView.as_view(), name='refresh-token'),
    path('verify-token/', TokenVerifyView.as_view(), name='verify-token')
]