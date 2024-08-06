from django.db import models


class TestModel(models.Model):
    district_code = models.CharField(max_length=10)
    district_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'schoolnew_district' 

        
class TestingPySchoolDetail(models.Model):
    school_id = models.AutoField(primary_key=True)
    # Add other fields as needed

    class Meta:
        db_table = 'testing_py_school_detail'

class TestingPyStu(models.Model):
    student_id = models.AutoField(primary_key=True)
    school_id = models.ForeignKey(TestingPySchoolDetail, on_delete=models.CASCADE,db_column='school_id',null=True)
    # Add other fields as needed

    class Meta:
        db_table = 'testing_py_stu'
        
class SchoolDet(models.Model):
    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'students_school_child_count'
        
class TeacherType(models.Model):
    id = models.AutoField(primary_key=True)
    type_teacher = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'teacher_type'

class TeacherDet(models.Model):
    u_id = models.AutoField(primary_key=True)
    teacher_id = models.CharField(max_length=100)
    school_key_id = models.ForeignKey(SchoolDet, on_delete=models.CASCADE,db_column='school_key_id',null=True)
    teacher_type = models.ForeignKey(TeacherType, on_delete=models.CASCADE, db_column='teacher_type',null=True)

    class Meta:
        db_table = 'udise_staffreg'

class CounsellingModel(models.Model):
    from_date = models.DateField(blank=True, null=True)
    to_date = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    directorate = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    counselling_type = models.CharField(max_length=255, blank=True, null=True)
    teacher_type = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    subject_nme = models.CharField(max_length=255, blank=True, null=True)
    scl_category = models.CharField(max_length=255, blank=True, null=True)
    scl_management = models.CharField(max_length=255, blank=True, null=True)
    scl_panel = models.CharField(max_length=255, blank=True, null=True)
    vac_category = models.CharField(max_length=255, blank=True, null=True)
    vac_management = models.CharField(max_length=255, blank=True, null=True)
    vac_panel = models.CharField(max_length=255, blank=True, null=True)
    level1_approver = models.CharField(max_length=255, blank=True, null=True)
    level2_approver = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    application_status = models.IntegerField(blank=True, null=True)
    vac_updated_by = models.CharField(max_length=255, blank=True, null=True)
    candidate_updated_by = models.CharField(max_length=255, blank=True, null=True)
    vacancy_publish_status = models.BooleanField()
    seniority_publish_status = models.BooleanField()
    seniority_chlg_status = models.BooleanField()
    vaccancy_chlg_status = models.BooleanField()
    pre_select_vaccancy = models.BooleanField()
    update_candidate_sts = models.BooleanField()
    seniority_reset_sts = models.BooleanField()
    seniority_order = models.IntegerField(blank=True, null=True)
    counselling_school_type = models.CharField(max_length=255, blank=True, null=True)
    counselling_minority = models.CharField(max_length=255, blank=True, null=True)
    vacancy_minority = models.CharField(max_length=255, blank=True, null=True)
    willing_sts = models.BooleanField()
    same_district_sts = models.BooleanField()
    isactive = models.BooleanField(default=True)

    
    class Meta:
        db_table = 'staff_counselling_mainpage'



