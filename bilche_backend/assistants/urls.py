from django.urls import path

from assistants.views import AddNewSiteAPIView, GetSitesAPIView

urlpatterns = [
    path('add_site/', AddNewSiteAPIView.as_view()),
    path('sites/', GetSitesAPIView.as_view()),
]