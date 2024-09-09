from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views.student_list import *
from .views.master import *

from app.auth import Auth

class CustomRouter(DefaultRouter):
    def get_default_basename(self, viewset):
        # Use the viewset class name as the basename
        return viewset.__class__.__name__
    
    


# Create a custom router
router = CustomRouter(trailing_slash=False)

router.register(r'', MasterAPIView)
router.register(r'', StudentAPIView)




# Define the URL patterns
urlpatterns = [
    path('', include(router.urls)),
    path('alldistrict', MasterAPIView.as_view({'get': 'district_list'},authentication_classes=[Auth])),
    path('schoollist', MasterAPIView.as_view({'get': 'school_list'},authentication_classes=[Auth])),
    path('studentlist', MasterAPIView.as_view({'get': 'student_list'},authentication_classes=[Auth])),
    path('schoollistdist', MasterAPIView.as_view({'get': 'school_list_by_dist'})),
    path('Classlist', StudentAPIView.as_view({'get': 'Classlist'},authentication_classes=[Auth])),
    path('StudScholarCheckTag', StudentAPIView.as_view({'get': 'StudScholarCheckTag'},authentication_classes=[Auth])),
    path('studentRegistration', StudentAPIView.as_view({'get': 'studentRegistration'},authentication_classes=[Auth])),
    path('OtpPurpose', StudentAPIView.as_view({'get': 'OtpPurpose'},authentication_classes=[Auth])),
    path('schoolWiseClassandSection', StudentAPIView.as_view({'get': 'schoolWiseClassandSection'},authentication_classes=[Auth])),
    path('classWiseStudentList', StudentAPIView.as_view({'post': 'classWiseStudentList'},authentication_classes=[Auth]))

]