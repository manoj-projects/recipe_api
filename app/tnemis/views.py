from django.http import JsonResponse
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from .services import *
from .serializers import *
from .models import *
from rest_framework import viewsets,status
import sys
# from rest_framework.permissions import AllowAny

class TestAPIView(viewsets.ViewSet):
    # permission_classes = [AllowAny]
    def district_list(self, request):
        try:
            result = CounsellingService.get_districts()
            serializer = TestSerializer(result, many=True)
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

    def CnslMainPageGetAll(self, request):
        
        counselling_id = request.GET.get('CnsId')
        try:
            result = CounsellingService.CnslMainPageGetAll(counselling_id)
        
            serializer= CounsellingSerializer(result, many=True)

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
            
    def Tchrdet(self,request):
        teacher_id = request.GET.get('TchrId')
        try:
            result = CounsellingService.Tchrdet(teacher_id)
            serializer= TchrSerializer(result, many=True)
            print(serializer.data)
            
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
    
    def CnslMainPage(self, request):
        records = request.data.get('records')
        
        if not records:
            return JsonResponse({
                "dataStatus": False,
                "status": 400,
                "message": "Records data is required"
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Extract data from records and map it to the fields expected by the serializer
            data = {
                'id': records.get('IndexId'),
                'from_date': records.get('FromDate'),
                'to_date': records.get('ToDate'),
                'title': records.get('Title'),
                'directorate': records.get('Directorate'),
                'location': records.get('Location'),
                'counselling_type': records.get('CounsellingType'),
                'teacher_type': records.get('TeacherType'),
                'designation': records.get('DesignationName'),
                'subject': records.get('Subject'),
                'subject_nme': records.get('SubjectName'),
                'scl_category': records.get('SclCategory'),
                'scl_management': records.get('SclManagement'),
                'scl_panel': records.get('SclPanel'),
                'vac_category': records.get('VacCategory'),
                'vac_management': records.get('VacManagement'),
                'vac_panel': records.get('VacPanel'),
                'level1_approver': records.get('Level1Approver'),
                'level2_approver': records.get('Level2Approver'),
                'status': records.get('Status'),
                'application_status': records.get('AppSts'),
                'vac_updated_by': records.get('VacUpdatedBy'),
                'candidate_updated_by': records.get('CandidateUpdatedBy'),
                'vacancy_publish_status': records.get('VacanyPublish'),
                'seniority_publish_status': records.get('SeniorityPublish'),
                'seniority_chlg_status': records.get('SeniorityChallenge'),
                'vaccancy_chlg_status': records.get('VacancyChallenge'),
                'pre_select_vaccancy': records.get('PreSelectVacancies'),
                'update_candidate_sts': records.get('UpdateCandidate'),
                'seniority_reset_sts': records.get('SeniorityReset'),
                'seniority_order': records.get('SeniorityOrder'),
                'counselling_school_type': records.get('schType'),
                'counselling_minority': records.get('counselling_minority'),
                'vacancy_minority': records.get('vacancy_minority'),
                'willing_sts': records.get('willing_sts'),
                'same_district_sts': records.get('same_district_sts')
            }
            
            # Apply filtering or transformation to the data if needed
            data = Common.Objfilter(data)
    
      
            # Determine the table name for the model
            tbl_name = 'staff_counselling_mainpage'

            if data.get('id'):
                # Update existing record if ID is provided
                instance = CounsellingModel.objects.get(id=data['id'])
                serializer = StaffCnsMainPageSerializer(instance, data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({
                        "dataStatus": True,
                        "status": 200,
                        "IndxID": serializer.data['id'],
                        "message": 'Updated Successfully'
                    }, status=status.HTTP_200_OK)
                else:
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                # Insert new record after checking for duplicates
                dupdata = {
                    'from_date': data['from_date'],
                    'to_date': data['to_date'],
                    'counselling_type': data['counselling_type'],
                    'teacher_type': data['teacher_type'],
                    'isactive': 1
                }

         
                if Common.check_duplicate(tbl_name, dupdata,CounsellingModel):
                    return JsonResponse({
                        "dataStatus": False,
                        "status": 409,
                        "message": 'Duplicate Entry'
                    }, status=status.HTTP_409_CONFLICT)

       
                serializer = StaffCnsMainPageSerializer(data=data)
              
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse({
                        "dataStatus": True,
                        "status": 200,
                        "IndxID": serializer.data['id'],
                        "message": 'Inserted Successfully'
                    }, status=status.HTTP_200_OK)
                else:
                    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return JsonResponse({
                "dataStatus": False,
                "status": 500,
                "message": str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
