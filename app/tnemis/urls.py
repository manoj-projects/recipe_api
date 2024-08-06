from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TestAPIView
from app.auth import Auth

class CustomRouter(DefaultRouter):
    def get_default_basename(self, viewset):
        # Use the viewset class name as the basename
        return viewset.__class__.__name__
    
    


# Create a custom router
router = CustomRouter(trailing_slash=False)

router.register(r'', TestAPIView)



# Define the URL patterns
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/alldistrict', TestAPIView.as_view({'get': 'district_list'},authentication_classes=[Auth]), name='district list api'),
    path('api/v1/CnslMainPageGetAll', TestAPIView.as_view({'get': 'CnslMainPageGetAll'},authentication_classes=[Auth]), name='counselling list api'),
    path('api/v1/Tchrdet', TestAPIView.as_view({'get': 'Tchrdet'},authentication_classes=[Auth]), name='teacher detail api'),
    path('api/v1/CnslMainPage', TestAPIView.as_view({'post': 'CnslMainPage'},authentication_classes=[Auth]), name='counselling list save api')
    
  
]