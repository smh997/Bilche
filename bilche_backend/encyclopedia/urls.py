from django.urls import path

from encyclopedia.views import SearchAPIView

urlpatterns = [
    path('search/', SearchAPIView.as_view()),
]