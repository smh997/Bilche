from django.urls import path

from encyclopedia.views import SearchAPIView, GetBasePlantAPIView, ReportEditPlantAPIView, FavoritePlantAPIView

urlpatterns = [
    path('search/', SearchAPIView.as_view()),
    path('plants/<int:pk>/', GetBasePlantAPIView.as_view()),
    path('plants/<int:id>/report_edit/', ReportEditPlantAPIView.as_view()),
    path('plants/<int:id>/favorite/', FavoritePlantAPIView.as_view()),
]