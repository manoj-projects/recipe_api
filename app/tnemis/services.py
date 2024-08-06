from .models import *
from .serializers import *
from django.db.models import F,OuterRef, Subquery,Value,Case, Value, When,Q
from django.db.models.functions import NullIf
from django.apps import apps

class CounsellingService:

    def get_districts(using='db_read'):
        try:
            return TestModel.objects.using(using).all()
        except Exception as e:
            print(f"An error occurred while fetching districts: {e}")
            return TestModel.objects.none()


    def CnslMainPageGetAll(counselling_id, using='db_read'):
        try:
            return CounsellingModel.objects.using(using).filter(id=counselling_id)
        except Exception as e:
            print(f"An error occurred while fetching counselling: {e}")
            return CounsellingModel.objects.none()
    
    def Tchrdet(teacher_id, using='db_read'):
        try:
            # result =  TestingPyStu.objects.select_related('school_id').all()
            result = TeacherDet.objects.select_related('school_key_id','teacher_type').all()
            result = result.filter(school_key_id=3509)
            return result
        except Exception as e:
            print(f"An error occurred while fetching counselling: {e}")
            return TestingPyStu.objects.none()
        
class Common:  
    
    def Objfilter(data):
     print(data)
     return {k: v for k, v in data.items() if v not in ["", None]}
     
 
    def empty(value):
        if value in [None, False, 0, 0.0, "0", "", [], {}, (), set()]:
            return True
        return False

    def check_duplicate(tbl_name, dupdata,ModelNme):
        # Query to check for duplicates based on provided criteria
        exists = ModelNme.objects.filter(
            from_date=dupdata['from_date'],
            to_date=dupdata['to_date'],
            counselling_type=dupdata['counselling_type'],
            teacher_type=dupdata['teacher_type'],
            isactive=1
        ).exists()
        
        return exists
            

                


