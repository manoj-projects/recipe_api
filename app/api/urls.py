from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import LoginViewSet

class CustomRouter(DefaultRouter):
    def get_default_basename(self, viewset):
        # Use the viewset class name as the basename
        return viewset.__class__.__name__

# Create a custom router
router = CustomRouter(trailing_slash=False)

router.register(r'', LoginViewSet)

# Define the URL patterns
urlpatterns = [
    # Include the router URLs under the 'api/v1/' prefix
    path('api/v1/', include(router.urls)),
    path('api/v1/login', LoginViewSet.as_view({'Post': 'login'}), name='login')
]
