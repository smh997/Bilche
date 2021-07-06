from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.schemas import get_schema_view as g
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
   openapi.Info(
      title="Bilche API",
      default_version='v1',
      description="Bilche.co",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="Bilche.tech@gmail.com"),
      license=openapi.License(name="Bilche License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/accounts/', include('accounts.urls')),
    path('api/home_page/', include('home_page.urls')),
    path('api/encyclopedia/', include('encyclopedia.urls')),
    path('api/assistants/', include('assistants.urls')),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/openapi/', g(), name='openapi-schema'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
