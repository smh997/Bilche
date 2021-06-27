from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from accounts.views import UserRegistrationAPIView

urlpatterns = [
    path('login/', view=obtain_auth_token),
    path('register/', view=UserRegistrationAPIView.as_view()),
]