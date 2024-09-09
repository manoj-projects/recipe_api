from django.db import models

# District model

class District(models.Model):
    id = models.AutoField(primary_key=True)
    district_code = models.IntegerField(unique=True)
    district_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=75, null=True, blank=True)
    short_name = models.CharField(max_length=4, null=True, blank=True)
    block_count = models.SmallIntegerField(null=True, blank=True)
    structure_freezed = models.BooleanField(default=False)
    district_name_tamil = models.CharField(max_length=500, null=True, blank=True)
    tnega_code = models.IntegerField(null=True, blank=True)
    lgd_code = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'schoolnew_district'
        

# School child count model

class StudentsSchoolChildCount(models.Model):
    id = models.AutoField(primary_key=True)
    school_id = models.IntegerField(null=True,blank=True,unique=True)
    district = models.ForeignKey(District, related_name='students_counts', on_delete=models.SET_NULL, null=True, blank=True)
    block_id = models.IntegerField(null=True, blank=True)
    edu_dist_id = models.IntegerField(null=True, blank=True)
    district_name = models.CharField(max_length=50, null=True, blank=True)
    block_name = models.CharField(max_length=100, null=True, blank=True)
    edu_dist_name = models.CharField(max_length=50, null=True, blank=True)
    udise_code = models.BigIntegerField(null=True, blank=True)
    school_name = models.CharField(max_length=200, null=True, blank=True)
    school_type = models.CharField(max_length=30, null=True, blank=True)
    school_type_id = models.IntegerField(null=True, blank=True)
    sch_directorate_id = models.BigIntegerField(null=True, blank=True)
    manage_id = models.IntegerField(null=True, blank=True)
    management = models.CharField(max_length=100, null=True, blank=True)
    cate_id = models.IntegerField(null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    catty_id = models.IntegerField(null=True, blank=True)
    cate_type = models.CharField(max_length=50, null=True, blank=True)
    board_id = models.IntegerField(default=0)
    board_name = models.CharField(max_length=50, null=True, blank=True)
    minority_sch = models.CharField(max_length=20, null=True, blank=True)
    minority_type = models.CharField(max_length=50, null=True, blank=True)
    sch_for_cwsn = models.CharField(max_length=20, null=True, blank=True)
    residential_sch = models.CharField(max_length=20, null=True, blank=True)
    shift_sch = models.CharField(max_length=20, null=True, blank=True)
    rte_sch = models.CharField(max_length=20, null=True, blank=True)
    type = models.IntegerField(default=3)
    dpi = models.CharField(max_length=5, null=True, blank=True)
    section_nos = models.IntegerField(default=0)
    low_class = models.IntegerField(default=0)
    high_class = models.IntegerField(default=0)
    prkg_b = models.IntegerField(default=0)
    prkg_g = models.IntegerField(default=0)
    prkg_t = models.IntegerField(default=0)
    prkg = models.IntegerField(default=0)
    lkg_b = models.IntegerField(default=0)
    lkg_g = models.IntegerField(default=0)
    lkg_t = models.IntegerField(default=0)
    lkg = models.IntegerField(default=0)
    ukg_b = models.IntegerField(default=0)
    ukg_g = models.IntegerField(default=0)
    ukg_t = models.IntegerField(default=0)
    ukg = models.IntegerField(default=0)
    c1_b = models.IntegerField(default=0)
    c1_g = models.IntegerField(default=0)
    c1_t = models.IntegerField(default=0)
    c1 = models.IntegerField(default=0)
    c2_b = models.IntegerField(default=0)
    c2_g = models.IntegerField(default=0)
    c2_t = models.IntegerField(default=0)
    c2 = models.IntegerField(default=0)
    c3_b = models.IntegerField(default=0)
    c3_g = models.IntegerField(default=0)
    c3_t = models.IntegerField(default=0)
    c3 = models.IntegerField(default=0)
    c4_b = models.IntegerField(default=0)
    c4_g = models.IntegerField(default=0)
    c4_t = models.IntegerField(default=0)
    c4 = models.IntegerField(default=0)
    c5_b = models.IntegerField(default=0)
    c5_g = models.IntegerField(default=0)
    c5_t = models.IntegerField(default=0)
    c5 = models.IntegerField(default=0)
    c6_b = models.IntegerField(default=0)
    c6_g = models.IntegerField(default=0)
    c6_t = models.IntegerField(default=0)
    c6 = models.IntegerField(default=0)
    c7_b = models.IntegerField(default=0)
    c7_g = models.IntegerField(default=0)
    c7_t = models.IntegerField(default=0)
    c7 = models.IntegerField(default=0)
    c8_b = models.IntegerField(default=0)
    c8_g = models.IntegerField(default=0)
    c8_t = models.IntegerField(default=0)
    c8 = models.IntegerField(default=0)
    c9_b = models.IntegerField(default=0)
    c9_g = models.IntegerField(default=0)
    c9_t = models.IntegerField(default=0)
    c9 = models.IntegerField(default=0)
    c10_b = models.IntegerField(default=0)
    c10_g = models.IntegerField(default=0)
    c10_t = models.IntegerField(default=0)
    c10 = models.IntegerField(default=0)
    c11_b = models.IntegerField(default=0)
    c11_g = models.IntegerField(default=0)
    c11_t = models.IntegerField(default=0)
    c11 = models.IntegerField(default=0)
    c12_b = models.IntegerField(default=0)
    c12_g = models.IntegerField(default=0)
    c12_t = models.IntegerField(default=0)
    c12 = models.IntegerField(default=0)
    total_b = models.IntegerField(default=0)
    total_g = models.IntegerField(default=0)
    total_t = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    bc = models.IntegerField(default=0)
    mbc = models.IntegerField(default=0)
    st = models.IntegerField(default=0)
    sc = models.IntegerField(default=0)
    oc = models.IntegerField(default=0)
    dnc = models.IntegerField(default=0)
    teach_tot = models.IntegerField(default=0)
    nonteach_tot = models.IntegerField(default=0)
    basic_service_staff_tot = models.IntegerField(default=0)
    admin_staff_tot = models.IntegerField(default=0)
    totstaff = models.IntegerField(default=0)
    habitation_id = models.IntegerField(null=True, blank=True)
    habitation_name = models.CharField(max_length=100, null=True, blank=True)
    localbody_id = models.IntegerField(null=True, blank=True)
    localbody_name = models.CharField(max_length=100, null=True, blank=True)
    localbody_type = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=True, blank=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=True, blank=True)
    beo_map = models.IntegerField(null=True, blank=True)
    beo_username = models.IntegerField(default=0)
    deo_map = models.IntegerField(default=0)
    deo_username = models.IntegerField(default=0)
    brte_id = models.IntegerField(default=0)
    urbanrural = models.CharField(max_length=20, default='Not Updated')
    taluk_id = models.IntegerField(default=0)
    taluk_name = models.CharField(max_length=100, null=True, blank=True)
    verification_status = models.IntegerField(null=True, blank=True)
    verification_date = models.DateField(null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)
    spl_educator_id = models.BigIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'students_school_child_count'
    
# Student child detail model

class StudentsChildDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    name_tamil = models.CharField(max_length=200, null=True, blank=True)
    name_id_card = models.CharField(max_length=200, null=True, blank=True)
    name_tamil_id_card = models.CharField(max_length=200, null=True, blank=True)
    aadhaar_uid_number = models.BigIntegerField(null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True) 
    dob = models.DateField(null=True, blank=True)
    community_id = models.IntegerField(null=True, blank=True)
    religion_id = models.IntegerField(null=True, blank=True)
    mothertounge_id = models.IntegerField(null=True, blank=True)
    phone_number = models.BigIntegerField(null=True, blank=True)
    differently_abled = models.IntegerField(null=True, blank=True)
    disadvantaged_group = models.IntegerField(null=True, blank=True)
    subcaste_id = models.IntegerField(null=True, blank=True)
    house_address = models.CharField(max_length=200, null=True, blank=True)
    pin_code = models.IntegerField(null=True, blank=True)
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    mother_name_tamil = models.CharField(max_length=50, null=True, blank=True)
    mother_occupation = models.CharField(max_length=50, null=True, blank=True)
    mother_qualify = models.IntegerField(null=True, blank=True)
    father_name = models.CharField(max_length=100, null=True, blank=True)
    father_name_tamil = models.CharField(max_length=200, null=True, blank=True)
    father_occupation = models.CharField(max_length=50, null=True, blank=True)
    father_qualify = models.IntegerField(null=True, blank=True)
    class_studying_id = models.IntegerField(null=True, blank=True)
    student_admitted_section = models.CharField(max_length=100, null=True, blank=True)
    group_code_id = models.IntegerField(null=True, blank=True)
    education_medium_id = models.IntegerField(null=True, blank=True)
    district_id = models.IntegerField(null=True, blank=True)
    unique_id_no = models.BigIntegerField(null=True, blank=True)
    school_id = models.IntegerField(null=True, blank=True)
    transfer_flag = models.IntegerField(null=True, blank=True)
    class_section = models.CharField(max_length=30, null=True, blank=True)
    school_admission_no = models.CharField(max_length=100, null=True, blank=True)
    guardian_name = models.CharField(max_length=100, null=True, blank=True)
    guardian_name_tamil = models.CharField(max_length=50, null=True, blank=True)
    guardian_qualify = models.IntegerField(null=True, blank=True)
    parent_income = models.IntegerField(null=True, blank=True)
    street_name = models.CharField(max_length=200, null=True, blank=True)
    area_village = models.CharField(max_length=200, null=True, blank=True)
    cbse_subject1_id = models.IntegerField(null=True, blank=True)
    cbse_subject2_id = models.IntegerField(null=True, blank=True)
    cbse_subject3_id = models.IntegerField(null=True, blank=True)
    cbse_subject4_id = models.IntegerField(default=0)
    cbse_opt_subject_id = models.IntegerField(default=0)
    doj = models.DateField(null=True, blank=True)
    pass_fail = models.CharField(max_length=8, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, null=True, blank=True) 
    prv_class_std = models.IntegerField(default=1)
    child_admitted_under_reservation = models.CharField(max_length=3, null=True, blank=True)
    rte_type = models.IntegerField(null=True, blank=True)
    idcardstatus = models.CharField(max_length=20, null=True, blank=True) 
    idapproove = models.CharField(max_length=1, default='0')
    adhaarappliedstatus = models.CharField(max_length=20, null=True, blank=True) 
    enrollmentnumber = models.BigIntegerField(null=True, blank=True)
    bloodgroup = models.IntegerField(null=True, blank=True)
    photo = models.CharField(max_length=50, null=True, blank=True)
    smart_id = models.CharField(max_length=20, null=True, blank=True)
    request_flag = models.CharField(max_length=1, null=True, blank=True) 
    request_date = models.DateField(null=True, blank=True)
    request_id = models.BigIntegerField(null=True, blank=True)
    c_exam = models.CharField(max_length=1, default='0') 
    age = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'students_child_detail'
        
        # Teacher table Udise staffreg model
class UdiseStaffReg(models.Model):
    u_id = models.BigAutoField(primary_key=True)
    teacher_id = models.IntegerField(null=True, blank=True,unique=True)
    off_code = models.IntegerField(null=True, blank=True)
    off_id = models.IntegerField(null=True, blank=True)
    district_id = models.IntegerField(null=True, blank=True)
    block_id = models.IntegerField(null=True, blank=True)
    udise_code = models.BigIntegerField(null=True, blank=True)
    school_key_id = models.IntegerField(null=True, blank=True)
    teacher_code = models.CharField(max_length=50, null=True, blank=True)
    aadhar_no = models.BigIntegerField(null=True, blank=True)
    cps_gps_details = models.CharField(max_length=20, null=True, blank=True)
    cps_gps = models.CharField(max_length=20, null=True, blank=True)
    suffix = models.IntegerField(null=True, blank=True)
    teacher_name = models.CharField(max_length=100, null=True, blank=True)
    teacher_name_tamil = models.CharField(max_length=100, null=True, blank=True, db_collation='utf8_unicode_ci')
    e_prnts_nme = models.CharField(max_length=200, null=True, blank=True)
    teacher_mother_name = models.CharField(max_length=100, null=True, blank=True)
    teacher_spouse_name = models.CharField(max_length=100, null=True, blank=True)
    e_med = models.CharField(max_length=200, null=True, blank=True)
    gender = models.IntegerField(null=True, blank=True)
    staff_dob = models.DateField(null=True, blank=True)
    staff_join = models.DateField(null=True, blank=True)
    staff_pjoin = models.DateField(null=True, blank=True)
    staff_psjoin = models.DateField(null=True, blank=True)
    e_doj_prpost = models.DateField(null=True, blank=True)
    social_category = models.IntegerField(null=True, blank=True)
    teacher_type = models.IntegerField(null=True, blank=True)
    user_type = models.IntegerField(null=True, blank=True)
    user_type1 = models.IntegerField(null=True, blank=True)
    appointment_nature = models.IntegerField(null=True, blank=True)
    academic = models.IntegerField(null=True, blank=True)
    professional = models.IntegerField(null=True, blank=True)
    class_taught = models.IntegerField(null=True, blank=True)
    appointed_subject = models.IntegerField(null=True, blank=True)
    subject1 = models.IntegerField(null=True, blank=True)
    subject2 = models.IntegerField(null=True, blank=True)
    subject3 = models.IntegerField(null=True, blank=True)
    subject4 = models.IntegerField(null=True, blank=True)
    subject5 = models.IntegerField(null=True, blank=True)
    subject6 = models.IntegerField(null=True, blank=True)
    deputed = models.IntegerField(null=True, blank=True)
    dep_place = models.IntegerField(null=True, blank=True)
    dep_off = models.IntegerField(null=True, blank=True)
    dep_scl = models.IntegerField(null=True, blank=True)
    dep_scldist = models.IntegerField(null=True, blank=True)
    dep_sclblk = models.IntegerField(null=True, blank=True)
    dep_date = models.DateField(null=True, blank=True)
    brc = models.IntegerField(null=True, blank=True)
    crc = models.IntegerField(null=True, blank=True)
    diet = models.IntegerField(null=True, blank=True)
    others = models.IntegerField(null=True, blank=True)
    trng_needed = models.IntegerField(default=0)
    trng_received = models.IntegerField(null=True, blank=True)
    nontch_days = models.IntegerField(default=0)
    math_upto = models.IntegerField(null=True, blank=True)
    science_upto = models.IntegerField(null=True, blank=True)
    english_upto = models.IntegerField(null=True, blank=True)
    soc_study_upto = models.IntegerField(null=True, blank=True)
    lang_study_upto = models.IntegerField(null=True, blank=True)
    wrkng_presentschlsince = models.IntegerField(null=True, blank=True)
    disability_type = models.IntegerField(null=True, blank=True)
    types_disability = models.IntegerField(null=True, blank=True)
    trained_cwsn = models.IntegerField(default=2)
    trained_comp = models.IntegerField(default=2)
    mbl_nmbr = models.BigIntegerField(null=True, blank=True)
    email_id = models.CharField(max_length=200, null=True, blank=True)
    e_prsnt_doorno = models.CharField(max_length=500, null=True, blank=True)
    e_prsnt_street = models.CharField(max_length=500, null=True, blank=True)
    e_prsnt_place = models.CharField(max_length=500, null=True, blank=True)
    e_prsnt_distrct = models.CharField(max_length=500, null=True, blank=True)
    e_prsnt_pincode = models.CharField(max_length=500, null=True, blank=True)
    e_blood_grp = models.CharField(max_length=500, null=True, blank=True)
    e_picid = models.BigIntegerField(null=True, blank=True)
    e_ug = models.CharField(max_length=500, null=True, blank=True)
    e_pg = models.CharField(max_length=500, null=True, blank=True)
    recruit_rank = models.CharField(max_length=20, null=True, blank=True)
    recruit_year = models.IntegerField(null=True, blank=True)
    scl_flag = models.CharField(max_length=1, null=True, blank=True)
    recruit_type = models.CharField(max_length=100, null=True, blank=True)
    posting_nature = models.CharField(max_length=10, null=True, blank=True)
    picid = models.IntegerField(null=True, blank=True)
    trans_category = models.CharField(max_length=300, null=True, blank=True)
    trans_remarks = models.CharField(max_length=400, null=True, blank=True)
    trans_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=1, null=True, blank=True)
    archive = models.IntegerField(null=True, blank=True)
    qr_code = models.CharField(max_length=10, null=True, blank=True)
    staff_img_name = models.TextField(null=True, blank=True)
    temp_login = models.BooleanField(default=False)
    temp_login_type = models.CharField(max_length=20, null=True, blank=True)
    main_teacher_id = models.IntegerField(null=True, blank=True)
    office_name = models.CharField(max_length=100, null=True, blank=True)
    office_address = models.CharField(max_length=100, null=True, blank=True)
    office_contact = models.BigIntegerField(null=True, blank=True)
    mbl_no = models.BigIntegerField(null=True, blank=True)
    dept = models.CharField(max_length=100, null=True, blank=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    ee_flag = models.BooleanField(null=True, blank=True)

    class Meta:
        db_table = 'udise_staffreg'
        
        # Admin  Udise Offreg model
class UdiseOffReg(models.Model):
    id = models.AutoField(primary_key=True)
    off_key_id = models.BigIntegerField(null=True, blank=True)
    office_user = models.CharField(max_length=30, null=True, blank=True)
    office_code = models.IntegerField(null=True, blank=True)
    district_id = models.IntegerField(null=True, blank=True)
    block_id = models.IntegerField(null=True, blank=True)
    edn_dist_id = models.IntegerField(null=True, blank=True)
    district_name = models.CharField(max_length=60, null=True, blank=True)
    block_name = models.CharField(max_length=60, null=True, blank=True)
    edudist_name = models.CharField(max_length=60, null=True, blank=True)
    office_type_id = models.IntegerField(null=True, blank=True)
    office_type = models.CharField(max_length=40, null=True, blank=True)
    office_area = models.TextField(null=True, blank=True)
    office_name = models.CharField(max_length=200, null=True, blank=True)
    institute_type = models.SmallIntegerField(null=True, blank=True)
    tamil_name = models.CharField(max_length=100, null=True, blank=True, db_collation='utf8_unicode_ci')
    officer_name = models.CharField(max_length=100, null=True, blank=True, db_collation='utf8_unicode_ci')
    officer_qualifi = models.CharField(max_length=100, null=True, blank=True, db_collation='utf8_unicode_ci')
    officer_mobile = models.CharField(max_length=30, null=True, blank=True)
    office_email = models.CharField(max_length=30, null=True, blank=True)
    office_landline = models.CharField(max_length=30, null=True, blank=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=True, blank=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=True, blank=True)
    isactive = models.SmallIntegerField(default=1)

    class Meta:
        db_table = 'udise_offreg'
  
  # Block model      
class SchoolNewBlock(models.Model):
    id = models.AutoField(primary_key=True)
    block_code = models.IntegerField()
    block_code_new = models.IntegerField(default=0)
    block_name = models.CharField(max_length=100)
    dee_block_name = models.CharField(max_length=100, null=True, blank=True)
    block_type = models.CharField(max_length=50)
    district_id = models.IntegerField()
    edu_dist_id = models.IntegerField(null=True, blank=True)
    beo_count = models.IntegerField(null=True, blank=True)
    cluster_count = models.SmallIntegerField(null=True, blank=True)
    school_count = models.SmallIntegerField(null=True, blank=True)
    mhrd_district_cd = models.IntegerField(default=33)
    dee_district = models.IntegerField(default=0)
    block_name_tamil = models.CharField(max_length=200, null=True, blank=True, db_collation='utf8mb4_unicode_ci')
    isactive = models.SmallIntegerField(null=True, blank=True)

    class Meta:
        db_table = 'schoolnew_block'
        
   # Class studying model
        
class BaseappClassStudying(models.Model):
    id = models.AutoField(primary_key=True)
    class_studying = models.CharField(max_length=10)
    sequence_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'baseapp_class_studying' 
        
         
        # section model
class SchoolNewSectionGroup(models.Model):
    id = models.AutoField(primary_key=True)
    school_key_id = models.IntegerField()
    class_id = models.ForeignKey('BaseappClassStudying', on_delete=models.SET_NULL,db_column='class_id', null=True)
    section = models.CharField(max_length=5, null=True, blank=True)
    no_of_periods = models.IntegerField(default=8)
    group_id = models.ForeignKey('BaseappGroupCode', on_delete=models.SET_NULL,db_column='group_id', null=True)
    school_type = models.IntegerField(null=True, blank=True)
    board_id = models.IntegerField(default=0)
    school_medium_id = models.ForeignKey('SchoolNewMediumOfInstruction', on_delete=models.SET_NULL,db_column='school_medium_id', null=True)
    students = models.IntegerField(null=True, blank=True)
    boys = models.SmallIntegerField(null=True, blank=True)
    girls = models.SmallIntegerField(null=True, blank=True)
    class_teacher_id = models.ForeignKey('UdiseStaffReg', on_delete=models.SET_NULL,db_column='class_teacher_id', null=True, to_field='teacher_id')
    pet_assigned = models.IntegerField(null=True, blank=True)
    isactive = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'schoolnew_section_group'
        
        #medium details model
        
class SchoolNewMediumOfInstruction(models.Model):
    ID = models.AutoField(primary_key=True)
    MEDINSTR_ID = models.IntegerField()
    MEDINSTR_DESC = models.CharField(max_length=75)
    MEDINSTR_PARENT = models.IntegerField()
    PREDEFINED = models.IntegerField(default=0)
    VISIBLE_YN = models.IntegerField(default=1)

    class Meta:
        db_table = 'schoolnew_mediumofinstruction'
        
        #school medium details model 
class SchoolMediumEntry(models.Model):
    id = models.AutoField(primary_key=True)
    school_key_id = models.IntegerField()
    medium_instrut = models.ForeignKey(SchoolNewMediumOfInstruction,on_delete=models.CASCADE,db_column='medium_instrut')
    other_medium = models.CharField(max_length=255)
    isactive = models.BooleanField()
        
    class Meta:
        db_table = 'schoolnew_mediumentry'
        
        # group code details model
class BaseappGroupCode(models.Model):
    id = models.AutoField(primary_key=True)
    group_code = models.IntegerField()
    sub1 = models.IntegerField(null=True, blank=True)
    sub2 = models.IntegerField(null=True, blank=True)
    sub3 = models.IntegerField(null=True, blank=True)
    sub4 = models.IntegerField(null=True, blank=True)
    sub5 = models.IntegerField(null=True, blank=True)
    sub6 = models.IntegerField(null=True, blank=True)
    group_name = models.CharField(max_length=500)
    group_description = models.TextField(null=True, blank=True)
    mhrd_id = models.IntegerField(null=True, blank=True)
    old_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'baseapp_group_code'
        
class BaseappGroupCodeCBSE(models.Model):
    id = models.AutoField(primary_key=True)
    group_code = models.IntegerField()
    group_name = models.CharField(max_length=500)
    
    class Meta:
        db_table = 'baseapp_group_code_cbse'
        
class BaseappBloodGroup(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.CharField(max_length=10)
    
    class Meta:
        db_table = 'baseapp_bloodgroup'        
        
        
class SchoolNewSchoolDepartment(models.Model):
    id = models.AutoField(primary_key=True) 
    department_code = models.CharField(max_length=10)
    department = models.CharField(max_length=100)
    school_mana_id = models.IntegerField()

    class Meta:
        db_table = 'schoolnew_school_department'
        
class SchoolNewManageCate(models.Model):
    id = models.AutoField(primary_key=True) 
    manage_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'schoolnew_manage_cate'
        


#school basic info model
class SchoolBasicInfo(models.Model):
    id = models.AutoField(primary_key=True)
    school_id = models.IntegerField(null=True, blank=True)
    old_udise_code = models.BigIntegerField(null=True, blank=True)
    udise_code = models.BigIntegerField(null=True, blank=True)
    school_name = models.CharField(max_length=200, null=True, blank=True)
    school_name_tamil = models.CharField(max_length=200, null=True, blank=True)
    sch_shortname = models.CharField(max_length=200, null=True, blank=True)
    district_id = models.IntegerField(null=True, blank=True)
    block_id = models.IntegerField(null=True, blank=True)
    urbanrural = models.IntegerField(null=True, blank=True)
    edu_dist_id = models.BigIntegerField(null=True, blank=True)
    manage_cate_id = models.ForeignKey(SchoolNewManageCate, on_delete=models.CASCADE, db_column='manage_cate_id', related_name='schoolnew_basic_mang')
    sch_management_id = models.IntegerField(null=True, blank=True)
    sch_cate_id = models.IntegerField(null=True, blank=True)
    sch_directorate_id = models.ForeignKey(SchoolNewSchoolDepartment,on_delete=models.CASCADE,db_column='sch_directorate_id',related_name='schoolnew_basicinfo')
    low_class = models.IntegerField(default=0)
    high_class = models.IntegerField(default=0)
    preprimary_yn = models.IntegerField(default=0)
    minority_yn = models.IntegerField(default=2)
    minority_type = models.IntegerField(default=0)
    minority_other = models.CharField(max_length=50, null=True, blank=True)
    special_sch_yn = models.IntegerField(default=2)
    special_sch_type = models.IntegerField(default=0)
    residential_yn = models.IntegerField(default=0)
    residential_type = models.IntegerField(default=0)
    shift_yn = models.IntegerField(default=0)
    location_type = models.IntegerField(default=0)
    rte = models.IntegerField(default=2)
    board_id = models.IntegerField(default=0)
    board_other = models.CharField(max_length=50, null=True, blank=True)
    board_aff_number = models.CharField(max_length=50, null=True, blank=True)
    local_body_id = models.IntegerField(null=True, blank=True)
    lb_vill_town_muni = models.IntegerField(null=True, blank=True)
    lb_habitation_id = models.BigIntegerField(null=True, blank=True)
    cluster_id = models.BigIntegerField(null=True, blank=True)
    panchayat_id = models.IntegerField(null=True, blank=True)
    municipal_id = models.IntegerField(null=True, blank=True)
    city_id = models.IntegerField(null=True, blank=True)
    corr_name = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    office_std_code = models.IntegerField(null=True, blank=True)
    office_landline = models.BigIntegerField(null=True, blank=True)
    corr_landline = models.BigIntegerField(null=True, blank=True)
    office_mobile = models.BigIntegerField(null=True, blank=True)
    corr_mobile = models.BigIntegerField(null=True, blank=True)
    corr_std_code = models.IntegerField(null=True, blank=True)
    sch_email = models.CharField(max_length=75, null=True, blank=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    latitude = models.DecimalField(max_digits=20, decimal_places=15, null=True, blank=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=15, null=True, blank=True)
    assembly_id = models.IntegerField(null=True, blank=True)
    parliament_id = models.IntegerField(null=True, blank=True)
    beo_map = models.IntegerField(null=True, blank=True)
    taluk_id = models.IntegerField(default=0)
    deo_map = models.SmallIntegerField(null=True, blank=True)
    cluster_index_id = models.IntegerField(default=0)
    student_id_count = models.BigIntegerField(null=True, blank=True)
    brte = models.BigIntegerField(default=0)
    school_code = models.BigIntegerField(null=True, blank=True)
    curr_stat = models.IntegerField(null=True, blank=True)
    curstat_date = models.DateField(null=True, blank=True)
    recog_status = models.SmallIntegerField(default=0)
    recog_upto = models.DateField(null=True, blank=True)
    app_status = models.IntegerField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    proceeding_no = models.CharField(max_length=50, null=True, blank=True)
    recog_doc = models.TextField(null=True, blank=True)
    affiliation_no = models.CharField(max_length=50, null=True, blank=True)
    emisofficial_schlmail = models.CharField(max_length=100, null=True, blank=True)
    temp_closed = models.SmallIntegerField(null=True, blank=True)
    rte_frm = models.CharField(max_length=10, null=True, blank=True)
    revenue_village_id = models.IntegerField(null=True, blank=True)
    lgd_subdistrict_id = models.IntegerField(null=True, blank=True)
    lgd_village_id = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'schoolnew_basicinfo'
        
#parent income model 
class BaseappParInc(models.Model):
    id = models.AutoField(primary_key=True)
    income_value = models.CharField(max_length=50)
   
    class Meta:
        db_table = 'baseapp_parentincome'

#religion model
class BaseappRelgion(models.Model):
    id = models.AutoField(primary_key=True)
    religion_name = models.CharField(max_length=50, null=True, blank=True)
    mhrd_item_id = models.IntegerField(null=True, blank=True)
    mhrd_sdmis_id = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'baseapp_religion'

#religion model
class TeacherAcademicQual(models.Model):
    id = models.AutoField(primary_key=True)
    academic_teacher = models.CharField(max_length=100, null=True, blank=True)
    visibility = models.IntegerField(null=True, blank=True)
    mhrd_id = models.IntegerField(null=True, blank=True)
    
    class Meta:
        db_table = 'teacher_academic_qualify'
        
#disadvantages model 
class BaseappDisAdvantage(models.Model):
    id = models.AutoField(primary_key=True)
    dis_group_name = models.CharField(max_length=100)
   
    class Meta:
        db_table = 'baseapp_disadvantaged_group'
        
#Differently Abled model
class BaseappDiffAbled(models.Model):
    id = models.AutoField(primary_key=True)
    da_code = models.IntegerField(null=True, blank=True)
    da_name = models.CharField(max_length=50, null=True, blank=True)
    mhrd_id = models.IntegerField(null=True, blank=True)
    cwsn_ph_one = models.TextField()
    
    class Meta:
        db_table = 'baseapp_differently_abled'
        
 #academic details       
class SchoolNewAcademicDetail(models.Model):
    id = models.AutoField(primary_key=True)
    school_key_id = models.IntegerField(null=True, blank=True)
    yr_estd_schl = models.IntegerField(null=True, blank=True)
    yr_rec_schl_elem = models.IntegerField(null=True, blank=True)
    yr_rec_schl_sec = models.IntegerField(null=True, blank=True)
    yr_rec_schl_hsc = models.IntegerField(null=True, blank=True)
    upgrad_prito_uprpri = models.IntegerField(null=True, blank=True)
    upgrad_uprprito_sec = models.IntegerField(null=True, blank=True)
    upgrad_secto_higsec = models.IntegerField(null=True, blank=True)
    yr_upgradprito_uprpri = models.IntegerField(null=True, blank=True)
    yr_upgraduprprito_sec = models.IntegerField(null=True, blank=True)
    yr_upgradsecto_higsec = models.IntegerField(null=True, blank=True)
    rte_pvt_c0_b = models.IntegerField(null=True, blank=True)
    rte_pvt_c0_g = models.IntegerField(null=True, blank=True)
    rte_pvt_c1_b = models.IntegerField(null=True, blank=True)
    rte_pvt_c1_g = models.IntegerField(null=True, blank=True)
    rte_pvt_c2_b = models.IntegerField(null=True, blank=True)
    rte_pvt_c2_g = models.IntegerField(null=True, blank=True)
    rte_pvt_c3_b = models.IntegerField(null=True, blank=True)
    rte_pvt_c3_g = models.IntegerField(null=True, blank=True)
    rte_pvt_c4_b = models.IntegerField(null=True, blank=True)
    rte_pvt_c4_g = models.IntegerField(null=True, blank=True)
    rte_pvt_c5_b = models.IntegerField(null=True, blank=True)
    rte_pvt_c5_g = models.IntegerField(null=True, blank=True)
    rte_pvt_c6_b = models.IntegerField(null=True, blank=True)
    rte_pvt_c6_g = models.IntegerField(null=True, blank=True)
    rte_pvt_c7_b = models.IntegerField(null=True, blank=True)
    rte_pvt_c7_g = models.IntegerField(null=True, blank=True)
    rte_pvt_c8_b = models.IntegerField(null=True, blank=True)
    rte_pvt_c8_g = models.IntegerField(null=True, blank=True)
    rte_bld_c0_b = models.IntegerField(null=True, blank=True)
    rte_bld_c0_g = models.IntegerField(null=True, blank=True)
    rte_bld_c1_b = models.IntegerField(null=True, blank=True)
    rte_bld_c1_g = models.IntegerField(null=True, blank=True)
    rte_bld_c2_b = models.IntegerField(null=True, blank=True)
    rte_bld_c2_g = models.IntegerField(null=True, blank=True)
    rte_bld_c3_b = models.IntegerField(null=True, blank=True)
    rte_bld_c3_g = models.IntegerField(null=True, blank=True)
    rte_bld_c4_b = models.IntegerField(null=True, blank=True)
    rte_bld_c4_g = models.IntegerField(null=True, blank=True)
    rte_bld_c5_b = models.IntegerField(null=True, blank=True)
    rte_bld_c5_g = models.IntegerField(null=True, blank=True)
    rte_bld_c6_b = models.IntegerField(null=True, blank=True)
    rte_bld_c6_g = models.IntegerField(null=True, blank=True)
    rte_bld_c7_b = models.IntegerField(null=True, blank=True)
    rte_bld_c7_g = models.IntegerField(null=True, blank=True)
    rte_bld_c8_b = models.IntegerField(null=True, blank=True)
    rte_bld_c8_g = models.IntegerField(null=True, blank=True)
    rte_ews_c9_b = models.IntegerField(null=True, blank=True)
    rte_ews_c9_g = models.IntegerField(null=True, blank=True)
    rte_ews_c10_b = models.IntegerField(null=True, blank=True)
    rte_ews_c10_g = models.IntegerField(null=True, blank=True)
    rte_ews_c11_b = models.IntegerField(null=True, blank=True)
    rte_ews_c11_g = models.IntegerField(null=True, blank=True)
    rte_ews_c12_b = models.IntegerField(null=True, blank=True)
    rte_ews_c12_g = models.IntegerField(null=True, blank=True)
    txtbk_recd_yn = models.IntegerField(null=True, blank=True)
    txtbk_recd_mon = models.IntegerField(null=True, blank=True)
    shftd_schl = models.IntegerField(null=True, blank=True)
    hill_frst = models.IntegerField(null=True, blank=True)
    spl_edtor = models.IntegerField(null=True, blank=True)
    resid_schl = models.IntegerField(null=True, blank=True)
    typ_resid_schl = models.IntegerField(null=True, blank=True)
    cwsn_scl = models.IntegerField(null=True, blank=True)
    renewal_valid = models.IntegerField(null=True, blank=True)
    yr_recgn_first = models.BigIntegerField(null=True, blank=True)
    yr_last_renwl = models.IntegerField(null=True, blank=True)
    yr_recogn_schl = models.IntegerField(null=True, blank=True)
    certifi_no = models.CharField(max_length=100, null=True, blank=True)
    prevoc_course = models.IntegerField(null=True, blank=True)
    school_type = models.CharField(max_length=10, null=True, blank=True)
    minority_sch = models.IntegerField(null=True, blank=True)
    minority_grp = models.IntegerField(null=True, blank=True)
    minority_other = models.CharField(max_length=50, null=True, blank=True)
    minority_yr = models.IntegerField(null=True, blank=True)
    scl_category = models.BigIntegerField(null=True, blank=True)
    low_class = models.PositiveSmallIntegerField(null=True, blank=True)
    high_class = models.PositiveSmallIntegerField(null=True, blank=True)
    electricity = models.IntegerField(null=True, blank=True)
    cal = models.IntegerField(null=True, blank=True)
    clab = models.IntegerField(null=True, blank=True)
    year_implmnt = models.IntegerField(null=True, blank=True)
    ict_lab = models.IntegerField(null=True, blank=True)
    model_ict = models.IntegerField(null=True, blank=True)
    ict_type = models.IntegerField(null=True, blank=True)
    internet = models.IntegerField(null=True, blank=True)
    acad_mnth_start = models.IntegerField(null=True, blank=True)
    rte = models.IntegerField(null=True, blank=True)
    rte_25p_applied = models.IntegerField(null=True, blank=True)
    rte_25p_enrolled = models.IntegerField(null=True, blank=True)
    mtongue_pri = models.IntegerField(null=True, blank=True)
    board_sec = models.IntegerField(null=True, blank=True)
    board_sec_no = models.CharField(max_length=50, null=True, blank=True)
    board_sec_oth = models.CharField(max_length=50, null=True, blank=True)
    board_hsec = models.IntegerField(null=True, blank=True)
    board_hsec_no = models.CharField(max_length=50, null=True, blank=True)
    board_hsec_oth = models.CharField(max_length=50, null=True, blank=True)
    distance_pri = models.CharField(max_length=5, null=True, blank=True)
    distance_upr = models.CharField(max_length=5, null=True, blank=True)
    distance_sec = models.CharField(max_length=5, null=True, blank=True)
    distance_hsec = models.CharField(max_length=5, null=True, blank=True)

    class Meta:
        db_table = 'schoolnew_academic_detail'

# rte model
class BaseappRteType(models.Model):
    id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=29)
    sub_category = models.CharField(max_length=18, blank=True, null=True)
    cat_id = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        db_table = 'baseapp_rte_type'

# department models        

        
        
       
        


        
