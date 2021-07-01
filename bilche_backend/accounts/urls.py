from django.urls import path
from accounts.views import UserRegistrationAPIView, MyObtainAuthToken, ResetPasswordAPIView, ResetPasswordConfirmAPIView

urlpatterns = [
    path('login/', view=MyObtainAuthToken.as_view()),
    path('register/', view=UserRegistrationAPIView.as_view()),
    path('password_reset/', ResetPasswordAPIView.as_view()),
    path('password_reset/confirm/', ResetPasswordConfirmAPIView.as_view()),
    # path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    # path('password_reset/confirm/', )
]