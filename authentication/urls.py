from django.urls import path
from authentication.views import User
# authentication urls

urlpatterns = [
    path('', User.as_view(), name='user'),
]