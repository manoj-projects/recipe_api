from django.db import models
from ..models.masters import * 

class SchoolNewTaggedList(models.Model):
    id = models.AutoField(primary_key=True)
    tag_id = models.IntegerField(default=0)
    school_id = models.ForeignKey(StudentsSchoolChildCount,on_delete=models.CASCADE,db_column='school_id',to_field='school_id',related_name='child_count')
    aeo_id = models.SmallIntegerField(null=True, blank=True)
    zone_id = models.SmallIntegerField(null=True, blank=True)
    academic_year = models.CharField(max_length=30, null=True, blank=True)
    curr_stat = models.IntegerField(default=1)
    flag = models.IntegerField(default=0)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    district_id = models.IntegerField(null=True, blank=True)
    district_name = models.CharField(max_length=100, null=True, blank=True)
    hud_id = models.IntegerField(null=True, blank=True)
    hud_name = models.CharField(max_length=100, null=True, blank=True)
    health_blk_id = models.IntegerField(null=True, blank=True)
    health_blk_name = models.CharField(max_length=100, null=True, blank=True)
    updated_by = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'schoolnew_tagged_list'
        
        
#otp
class BaseappOtpPurpose(models.Model):
    otp_purpose_id = models.AutoField(primary_key=True) 
    otp_purpose = models.CharField(max_length=200, null=True, blank=True)
    isactive = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'baseapp_otp_purpose'