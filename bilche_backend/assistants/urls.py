from django.urls import path

from assistants.views import AddNewSiteAPIView, GetSitesAPIView, SiteAPIView, AddNewPlantAPIView, PlantAPIView

urlpatterns = [
    path('add_site/', AddNewSiteAPIView.as_view()),
    path('sites/', GetSitesAPIView.as_view()),
    path('sites/<int:site_id>/', SiteAPIView.as_view()),
    path('sites/<int:site_id>/add_plant/', AddNewPlantAPIView.as_view()),
    path('plants/<int:plant_id>/', PlantAPIView.as_view()),
]