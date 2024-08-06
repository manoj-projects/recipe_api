from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django admin interface
    path('admin/', admin.site.urls),

    # API schema endpoint
    path('api/schema/', SpectacularAPIView.as_view(), name='api-schema'),

    # API documentation endpoint using Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='api-schema'), name='api-docs'),

    # Including API URLs from 'api.urls'
    path('', include('api.urls')),
    
    # Including API URLs from 'api.urls'
    path('', include('tnemis.urls')),
]
