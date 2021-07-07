from django.urls import path

from assistants.views import AddNewSiteAPIView

urlpatterns = [
    path('add_site/', AddNewSiteAPIView.as_view()),

]