from django.urls import path

from encyclopedia.views import SearchAPIView, GetBasePlantAPIView

urlpatterns = [
    path('search/', SearchAPIView.as_view()),
    path('plants/<int:pk>/', GetBasePlantAPIView.as_view())
]