from rest_framework import serializers
from .models import *

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestModel
        fields = ['id', 'district_code', 'district_name']  
        
class CounsellingSerializer(serializers.ModelSerializer):
    IndexId = serializers.IntegerField(source='id')
    FromDate = serializers.DateField(source='from_date')
    ToDate = serializers.DateField(source='to_date')
    Title = serializers.CharField(source='title')
    CounsellingType = serializers.CharField(source='counselling_type')
    Loc = serializers.CharField(source='location')
    Designation = serializers.CharField(source='teacher_type')
    DesignationName = serializers.CharField(source='designation')
    SubjectName = serializers.CharField(source='subject_nme')
    Subject = serializers.CharField(source='subject')
    SclCategory = serializers.CharField(source='scl_category')
    SclManagement = serializers.CharField(source='scl_management')
    SclPanel = serializers.CharField(source='scl_panel')
    Directorate = serializers.CharField(source='directorate')
    Status = serializers.CharField(source='status')
    Level1Approver = serializers.CharField(source='level1_approver')
    Level2Approver = serializers.CharField(source='level2_approver')
    AppSts = serializers.CharField(source='application_status')
    VacCategory = serializers.CharField(source='vac_category')
    VacManagement = serializers.CharField(source='vac_management')
    VacPanel = serializers.CharField(source='vac_panel')
    SeniorityOrder = serializers.IntegerField(source='seniority_order')
    Rule = serializers.CharField(source='rule')
    VacUpdatedBy = serializers.CharField(source='vac_updated_by')
    SchType = serializers.CharField(source='counselling_school_type')
    CounsellingMinority = serializers.CharField(source='counselling_minority')
    VacancyMinority = serializers.CharField(source='vacancy_minority')
    CandidateUpdatedBy = serializers.CharField(source='candidate_updated_by')
    VacanyPublish = serializers.CharField(source='vacancy_publish_status')
    SeniorityReset = serializers.CharField(source='seniority_reset_sts')
    SeniorityPublish = serializers.CharField(source='seniority_publish_status')
    SeniorityChallenge = serializers.CharField(source='seniority_chlg_status')
    VacancyChallenge = serializers.CharField(source='vaccancy_chlg_status')

    class Meta:
        model = CounsellingModel
        fields = ('IndexId', 'FromDate', 'ToDate', 'Title', 'CounsellingType', 'Loc', 'Designation', 'DesignationName', 'SubjectName', 
                  'Subject', 'SclCategory', 'SclManagement', 'SclPanel', 'Directorate', 'Status', 'Level1Approver', 'Level2Approver', 
                  'AppSts', 'VacCategory', 'VacManagement', 'VacPanel', 'SeniorityOrder', 'Rule', 'VacUpdatedBy', 'SchType', 
                  'CounsellingMinority', 'VacancyMinority', 'CandidateUpdatedBy', 'VacanyPublish', 'SeniorityReset', 
                  'SeniorityPublish', 'SeniorityChallenge', 'VacancyChallenge')

class TchrSerializer(serializers.ModelSerializer):
    
    TchrId= serializers.CharField(source='teacher_id')
    SchlId= serializers.CharField(source='school_key_id.school_id')
    SchlNme= serializers.CharField(source='school_key_id.school_name')
    TchrType = serializers.CharField(source='teacher_type.type_teacher',required=False)

     
    class Meta:
        model = TeacherDet
        fields = ['TchrId','SchlId','SchlNme','TchrType'] 
        
        
class StaffCnsMainPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CounsellingModel
        fields = '__all__'
        extra_kwargs = {
        'id': {'required': False, 'allow_null': True},
        'from_date': {'required': False, 'allow_null': True},
        'to_date': {'required': False, 'allow_null': True},
        'title': {'required': False, 'allow_null': True},
        'directorate': {'required': False, 'allow_null': True},
        'location': {'required': False, 'allow_null': True},
        'counselling_type': {'required': False, 'allow_null': True},
        'teacher_type': {'required': False, 'allow_null': True},
        'designation': {'required': False, 'allow_null': True},
        'subject': {'required': False, 'allow_null': True},
        'subject_nme': {'required': False, 'allow_null': True},
        'scl_category': {'required': False, 'allow_null': True},
        'scl_management': {'required': False, 'allow_null': True},
        'scl_panel': {'required': False, 'allow_null': True},
        'vac_category': {'required': False, 'allow_null': True},
        'vac_management': {'required': False, 'allow_null': True},
        'vac_panel': {'required': False, 'allow_null': True},
        'level1_approver': {'required': False, 'allow_null': True},
        'level2_approver': {'required': False, 'allow_null': True},
        'status': {'required': False, 'allow_null': True},
        'application_status': {'required': False, 'allow_null': True},
        'vac_updated_by': {'required': False, 'allow_null': True},
        'candidate_updated_by': {'required': False, 'allow_null': True},
        'vacancy_publish_status': {'required': False, 'allow_null': True},
        'seniority_publish_status': {'required': False, 'allow_null': True},
        'seniority_chlg_status': {'required': False, 'allow_null': True},
        'vaccancy_chlg_status': {'required': False, 'allow_null': True},
        'pre_select_vaccancy': {'required': False, 'allow_null': True},
        'update_candidate_sts': {'required': False, 'allow_null': True},
        'seniority_reset_sts': {'required': False, 'allow_null': True},
        'seniority_order': {'required': False, 'allow_null': True},
        'counselling_school_type': {'required': False, 'allow_null': True},
        'counselling_minority': {'required': False, 'allow_null': True},
        'vacancy_minority': {'required': False, 'allow_null': True},
        'willing_sts': {'required': False, 'allow_null': True},
        'same_district_sts': {'required': False, 'allow_null': True},
    }
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {key: value for key, value in data.items() if value is not None}






