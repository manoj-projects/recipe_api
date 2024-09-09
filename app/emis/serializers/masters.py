from .base import BaseSerializer
from ..models import *
from rest_framework import serializers

class DistrictSerializer(BaseSerializer):
    class Meta:
        model = District
        fields = '__all__'
        
class StuSchlChldCntSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentsSchoolChildCount
        fields = ('low_class', 'high_class')

class StuSchlChldCntallSerializer(BaseSerializer):
    class Meta:
        model = StudentsSchoolChildCount
        fields = '__all__'
        
class SchoolMediumOfInstructionSerializer(serializers.ModelSerializer):
    
    ID = serializers.IntegerField(source='medium_instrut__ID')
    MEDINSTR_ID = serializers.IntegerField(source='medium_instrut__MEDINSTR_ID')
    MEDINSTR_DESC = serializers.CharField(source='medium_instrut__MEDINSTR_DESC')
    MEDINSTR_PARENT = serializers.IntegerField(source='medium_instrut__MEDINSTR_PARENT')
    PREDEFINED = serializers.IntegerField(source='medium_instrut__PREDEFINED')
    VISIBLE_YN = serializers.IntegerField(source='medium_instrut__VISIBLE_YN')

    class Meta:
        model = SchoolNewMediumOfInstruction
        fields = ['ID', 'MEDINSTR_ID', 'MEDINSTR_DESC', 'MEDINSTR_PARENT', 'PREDEFINED','VISIBLE_YN']
        
        

class StuChldDetlSerializer(BaseSerializer):
    class Meta:
        model = StudentsChildDetail
        fields = '__all__'
        
        
        
class SchoolNewSectionGroupSimpleSerializer(serializers.ModelSerializer):
    class_studying = serializers.CharField(source='class_id.class_studying')
    sequence_id = serializers.IntegerField(source='class_id.sequence_id')
    MEDINSTR_ID = serializers.IntegerField(source='school_medium_id.MEDINSTR_ID')
    MEDINSTR_DESC = serializers.CharField(source='school_medium_id.MEDINSTR_DESC')
    group_code = serializers.CharField(source='group_id.group_code', default=None)
    group_name = serializers.CharField(source='group_id.group_name', default=None)
    teacher_name = serializers.CharField(source='class_teacher_id.teacher_name', default=None)
    teacher_id = serializers.CharField(source='class_teacher_id.teacher_id', default=None)
    TchrType = serializers.CharField(source='class_teacher_id.teacher_type', default=None)
    
    classSec = serializers.SerializerMethodField()


    class Meta:
        model = SchoolNewSectionGroup
        fields = (
            'id',
            'school_key_id',
            'section',
            'no_of_periods',
            'group_id',
            'school_type',
            'board_id',
            'school_medium_id',
            'students',
            'boys',
            'girls',
            'class_teacher_id',
            'pet_assigned',
            'class_studying',  
            'sequence_id',
            'MEDINSTR_ID',
            'MEDINSTR_DESC',
            'group_code',
            'group_name',
            'teacher_name',
            'teacher_id',
            'TchrType',
            'classSec'
        )

    def get_classSec(self, obj):

        class_studying = getattr(obj.class_id, 'class_studying', 'N/A') if obj.class_id else 'N/A'
        section = getattr(obj, 'section', 'N/A') if obj.class_id else 'N/A'
        
        return f"{class_studying}-{section}".strip()
        
        

    
class BaseappGrpSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseappGroupCode
        fields = '__all__'

class BaseappGrpCBSESerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseappGroupCodeCBSE
        fields = '__all__'
        
class BaseappBloodGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseappBloodGroup
        fields = '__all__'

class BasicinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolBasicInfo
        fields = ['manage_cate_id']
        


class SchoolNewSectionGroupSerializer(serializers.ModelSerializer):
    classSec = serializers.SerializerMethodField()
    School_Type = serializers.CharField(source='get_school_type_display')
    MEDINSTR_DESC = serializers.CharField(source='school_medium_id.MEDINSTR_DESC')
    Group_name = serializers.CharField(source='group_id.group_name')
    Group_code = serializers.CharField(source='group_id.group_code')
    class_studying = serializers.CharField(source='class_id.class_studying')

    class Meta:
        model = SchoolNewSectionGroup
        fields = (
            'district_id',
            'district_name',
            'block_name',
            'school_name',
            'class_id',
            'section',
            'classSec',
            'udise_code',
            'School_Type',
            'MEDINSTR_DESC',
            'Group_name',
            'Group_code',
            'Students'
        )

    def get_classSec(self, obj):
        return f"{obj.class_id.class_studying}-{obj.section}"