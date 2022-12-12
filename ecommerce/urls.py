from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view  
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view = swagger_get_schema_view(
    openapi.Info(
        title='Ecommerce',
        default_version='1.0.0',
        description='Ecommerce App',
    ),
    public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecommerce.inventory.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-schema'),
]  
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)