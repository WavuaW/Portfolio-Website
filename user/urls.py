from django.urls import path
from user.views import RegisterView
# route for user account creation

urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
]