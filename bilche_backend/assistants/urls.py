from django.urls import path

from assistants.views import AddNewSiteAPIView, GetSitesAPIView, SiteAPIView

urlpatterns = [
    path('add_site/', AddNewSiteAPIView.as_view()),
    path('sites/', GetSitesAPIView.as_view()),
    path('sites/<int:pk>/', SiteAPIView.as_view()),
]