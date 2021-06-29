from django.urls import path, include
from accounts.views import UserRegistrationAPIView, MyObtainAuthToken

urlpatterns = [
    path('login/', view=MyObtainAuthToken.as_view()),
    path('register/', view=UserRegistrationAPIView.as_view()),
]