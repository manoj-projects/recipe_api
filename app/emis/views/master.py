from django.http import JsonResponse
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from drf_spectacular.utils import extend_schema, OpenApiResponse
# from .services import *
from ..serializers.masters import *
from ..serializers.base import *
from ..models import *
from rest_framework import viewsets,status
from django.db.models import F, Value, CharField,Q,Sum, Case, When
from django.db.models.functions import Concat,Coalesce
import sys


class MasterAPIView(viewsets.ViewSet):
    @extend_schema(
        summary="Get a list of districts",
        description="Fetches a list of all districts.",
        responses={
            200: OpenApiResponse(
                response=DistrictSerializer(many=True),
                description="List of districts with transformed field names"
            ),
            500: OpenApiResponse(description="Internal Server Error"),
        }
    )
    def district_list(self, request):
        try:

            result = District.objects.all()
            serializer = DistrictSerializer(result, many=True)
            return JsonResponse({
                "dataStatus": True,
                "status": 200,
                "message": serializer.data
            })
        except Exception as e:
            return JsonResponse({
                "dataStatus": False,
                "status": 500,
                "message": f"{str(e)}"
            })        
            
    def school_list(self, request):
        try:
            school_id = request.GET.get('SchlId', None)
            district_id = request.GET.get('DistId', None)

            result = StudentsSchoolChildCount.objects.all()
            if school_id is not None:
                result = result.filter(school_id=school_id)
            if district_id is not None:
                result = result.filter(district_id=district_id)
                
            serializer = StuSchlChldCntSerializer(result, many=True)
            return JsonResponse({
                "dataStatus": True,
                "status": 200,
                "message": serializer.data
            })
        except Exception as e:
            return JsonResponse({
                "dataStatus": False,
                "status": 500,
                "message": f"{str(e)}"
            })
            
    def student_list(self, request):
        try:
            school_id = request.GET.get('SchlId')
            class_id = request.GET.get('Class')
            filters = {} 
            fields=['school_id', 'class_studying_id', 'name']  

            filters['school_id'] = school_id
            filters['class_studying_id'] = class_id

            result = StudentsChildDetail.objects.filter(**filters).values(*fields)
            print(result.query,'sql_query')
            data = list(result)
            serializer = BaseSerializer(data, many=True, fields=fields)
            return JsonResponse({
                "dataStatus": True,
                "status": 200,
                "message": serializer.data
            })
        except Exception as e:
            return JsonResponse({
                "dataStatus": False,
                "status": 500,
                "message": f"{str(e)}"
            })

    def school_list_by_dist(self,request):
        try:
            district_id = request.GET.get('DistId', None)
            
            if not district_id:
                return JsonResponse({
                    "dataStatus": False,
                    "status": 400,
                    "message": "District ID is required."
                })

            # Define which fields to include in the result
            fields = ['school_id', 'district__id', 'district__district_name', 'block_id']

            # Query the data
            result = (
                StudentsSchoolChildCount.objects
                .filter(district_id=district_id)
                .select_related('district')
                .values(*fields)
            )

            serializer=custom_serializer(result)
   

            return JsonResponse({
                "dataStatus": True,
                "status": 200,
                "message": serializer
            })
        
        except Exception as e:
            return JsonResponse({
                "dataStatus": False,
                "status": 500,
                "message": str(e)
            })
            
            

    
    
                
        