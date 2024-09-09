from rest_framework import serializers
from .base import BaseSerializer
from ..models.masters import *
from ..models.student_model import *

class SchoolNewTaggedSerializer(serializers.ModelSerializer): 
    class Meta:
        model = SchoolNewTaggedList
        fields = '__all__'
        
class IncomeSerializer(serializers.ModelSerializer): 
    class Meta:
        model = BaseappParInc
        fields = '__all__'
        
class ReligionSerializer(serializers.ModelSerializer): 
    class Meta:
        model = BaseappRelgion
        fields = '__all__'

class LanguagesSerializer(serializers.ModelSerializer): 
    class Meta:
        model = SchoolNewMediumOfInstruction
        fields = ('ID', 'MEDINSTR_DESC', 'MEDINSTR_ID')
        
class DisAdvantageSerializer(serializers.ModelSerializer): 
    class Meta:
        model = BaseappDisAdvantage
        fields = '__all__'

class DiffAbledSerializer(serializers.ModelSerializer): 
    class Meta:
        model = BaseappDiffAbled
        fields = '__all__'
        
class SchlDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'
        
class ClassStudySerializer(serializers.Serializer):
    class Meta:
        model = BaseappClassStudying
        fields = '__all__'

class SchlMedOfInstSerializer(serializers.ModelSerializer):
    
    ID = serializers.IntegerField(source='medium_instrut__ID')
    MEDINSTR_ID = serializers.IntegerField(source='medium_instrut__MEDINSTR_ID')
    MEDINSTR_DESC = serializers.CharField(source='medium_instrut__MEDINSTR_DESC')
    MEDINSTR_PARENT = serializers.IntegerField(source='medium_instrut__MEDINSTR_PARENT')
    PREDEFINED = serializers.IntegerField(source='medium_instrut__PREDEFINED')
    VISIBLE_YN = serializers.IntegerField(source='medium_instrut__VISIBLE_YN')

    class Meta:
        model = SchoolMediumEntry
        fields = ['ID', 'MEDINSTR_ID', 'MEDINSTR_DESC', 'MEDINSTR_PARENT', 'PREDEFINED','VISIBLE_YN','id','school_key_id','other_medium','isactive']
        
class RteSerializer(serializers.ModelSerializer):
    
    cate = serializers.SerializerMethodField()

    class Meta:
        model = BaseappRteType
        fields = ['cate', 'id']
        
    def get_cate(self, obj):
        return f"{obj.category}-{obj.sub_category or ''}"

class TeacherAcademicQualSer(serializers.ModelSerializer):
    class Meta:
        model = TeacherAcademicQual
        fields = '__all__'

class BaseappOtpPurposeSer(serializers.ModelSerializer):
    Otp_prps_id = serializers.IntegerField(source='otp_purpose_id')  
    Otp_prps = serializers.CharField(source='otp_purpose')          

    class Meta:
        model = BaseappOtpPurpose
        fields = ['Otp_prps_id', 'Otp_prps']
        

  