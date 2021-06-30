from django.urls import path

from home_page.views import FeedbackAPIView, SubscribeAPIView, InstallappAPIView

urlpatterns = [
    path('feedback/', FeedbackAPIView.as_view()),
    path('subscribe/', SubscribeAPIView.as_view()),
    path('installapp/', InstallappAPIView.as_view()),
]