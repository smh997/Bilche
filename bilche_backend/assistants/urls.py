from django.urls import path

from assistants.views import AddNewSiteAPIView, GetSitesAPIView, SiteAPIView, AddNewPlantAPIView

urlpatterns = [
    path('add_site/', AddNewSiteAPIView.as_view()),
    path('sites/', GetSitesAPIView.as_view()),
    path('sites/<int:site_id>/', SiteAPIView.as_view()),
    path('sites/<int:site_id>/add_plant/', AddNewPlantAPIView.as_view())
]