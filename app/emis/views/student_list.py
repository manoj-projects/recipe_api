from django.http import JsonResponse
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
from drf_spectacular.utils import extend_schema, OpenApiResponse
# from .services import *
from ..serializers.masters import *
from ..serializers.student_serializer import *
from ..serializers.base import *
from ..models import *
from ..models.student_model import *
from rest_framework import viewsets,status
from django.db.models import F, Value, CharField,Q,Sum, Case, When,IntegerField
from django.db.models.functions import Concat,Coalesce
from collections import defaultdict

import sys,json

class StudentAPIView(viewsets.ViewSet):
    def Classlist(self, request):
            
            
            try:
                token_details = getattr(request, 'tokenDetails', None)
                print(token_details,'jdfkdjfkdjfk') 
                SchlId = request.GET.get('school_id', None)
                    
                classlist = SchoolNewSectionGroup.objects.filter(
                    school_key_id=SchlId,
                    isactive=True,
                    class_teacher_id__archive__in=[1, 3]
                ).select_related(
                    'class_id', 'group_id', 'school_medium_id', 'class_teacher_id'
                ).annotate(
                            classSec=Concat(F('class_id__class_studying'), Value('-'), F('section')),
                            classid=F('class_id__id')
                        ).only(
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
                    'class_id__class_studying',
                    'class_id__sequence_id',
                    'school_medium_id__MEDINSTR_ID',
                    'school_medium_id__MEDINSTR_DESC',
                    'group_id__group_code',
                    'group_id__group_name',
                    'class_teacher_id__teacher_name',
                    'class_teacher_id__teacher_id',
                    'class_teacher_id__teacher_type'
                ).order_by('class_id__class_studying')


                print(classlist.query)

                classlist_ser = SchoolNewSectionGroupSimpleSerializer(classlist, many=True)
                
                classtype = StudentsSchoolChildCount.objects.filter(school_id=SchlId).only('low_class','high_class')
                
                classtype_ser = StuSchlChldCntSerializer(classtype,many=True)
                
                classmedium = SchoolMediumEntry.objects.filter(
                                Q(isactive=True) & Q(school_key_id=SchlId)
                            ).select_related('medium_instrut').values(
                                'medium_instrut__ID',           
                                'medium_instrut__MEDINSTR_ID',
                                'medium_instrut__MEDINSTR_DESC',
                                'medium_instrut__MEDINSTR_PARENT',
                                'medium_instrut__PREDEFINED',
                                'medium_instrut__VISIBLE_YN',
                                'id',
                                'school_key_id',
                                'medium_instrut',
                                'other_medium',
                                'isactive'
                            )

                classmedium_ser = SchoolMediumOfInstructionSerializer(classmedium, many=True)
                
                groupname=BaseappGroupCode.objects.filter(group_description=1)
                groupname_ser=BaseappGrpSerializer(groupname,many=True)
                
                schoolcate=SchoolBasicInfo.objects.filter(school_id=SchlId).only('manage_cate_id')
                
                schoolcate_ser=BasicinfoSerializer(schoolcate,many=True)
                
                
                
                return JsonResponse({
                    "dataStatus": True,
                    "status": 200,
                    "classlist": classlist_ser.data,
                    "classtype": classtype_ser.data,
                    "mediumdetails": classmedium_ser.data,
                    "groupdetails": groupname_ser.data,
                    "schoolcate": schoolcate_ser.data
                })
            except Exception as e:
                return JsonResponse({
                    "dataStatus": False,
                    "status": 500,
                    "message": f"{str(e)}"
                })  
                
    def StudScholarCheckTag(self, request):
              
            try:

                SchlId = request.GET.get('SchoolId', None)
            
                    
                transport = SchoolNewTaggedList.objects.filter(school_id=SchlId,tag_id=12).values('school_id')
              
                transport_exists = transport.exists()

                kgv = SchoolNewTaggedList.objects.filter(
                    Q(school_id__manage_id__in=[32, 36]) | Q(tag_id=13),
                    school_id=SchlId
                ).values('school_id')
                
                kgv_exists = kgv.exists()

                
                kgv_res = 1 if kgv_exists else 0
                transport_res = 1 if transport_exists else 0

                return JsonResponse({
                    "dataStatus": True,
                    "status": 200,
                    "kgbv": kgv_res,
                    "transport": transport_res
                })

            except Exception as e:
                return JsonResponse({
                    "dataStatus": False,
                    "status": 500,
                    "message": str(e)
                })
    
    def studentRegistration(self, request):
            
            
            try:
                token_details = getattr(request, 'tokenDetails', None)
                print(token_details,'jdfkdjfkdjfk') 
                SchlId = request.GET.get('school_id', None)
                    
                incomes=BaseappParInc.objects.all()

                incomes_ser = IncomeSerializer(incomes, many=True)
                
                religion=BaseappRelgion.objects.all()

                religion_ser = ReligionSerializer(religion, many=True)
                
                ordering = Case(
                                When(MEDINSTR_ID=4, then=1),
                                When(MEDINSTR_ID=3, then=2),
                                When(MEDINSTR_ID=17, then=3),
                                When(MEDINSTR_ID=5, then=4),
                                When(MEDINSTR_ID=8, then=5),
                                When(MEDINSTR_ID=16, then=6),
                                output_field=IntegerField(),
                            )

                launguages = SchoolNewMediumOfInstruction.objects.annotate(
                    custom_order=ordering
                ).order_by('-custom_order').values('ID', 'MEDINSTR_DESC', 'MEDINSTR_ID')
                
                launguages_ser = LanguagesSerializer(launguages, many=True)
                
                disadvantages=BaseappDisAdvantage.objects.all()

                disadvantages_ser = DisAdvantageSerializer(disadvantages, many=True)
                
                disabilities=BaseappDiffAbled.objects.all()

                disabilities_ser = DiffAbledSerializer(disabilities, many=True)
                
                schooldist = District.objects.all().order_by('district_name')
                
                schooldist_ser = SchlDistrictSerializer(schooldist, many=True)
        
                
                classlist = SchoolNewAcademicDetail.objects.filter(school_key_id=SchlId).only('id', 'low_class', 'high_class')

                if classlist.exists():
                    low_class = classlist.first().low_class
                    high_class = classlist.first().high_class

                    # Base query
                    base_query = BaseappClassStudying.objects.filter(
                        Q(id__range=(low_class, high_class)) & ~Q(class_studying='NA')
                    ).values('id', 'class_studying')

                    # Case query with condition to exclude 'NA'
                    case_query = BaseappClassStudying.objects.annotate(
                                new_id=Case(
                                    When(id=low_class, then=Value(0)),
                                    default=F('id'),
                                    output_field=IntegerField()
                                ),
                                new_class_studying=Case(
                                    When(id=low_class, then=Value('NA')),
                                    default=F('class_studying'),
                                    output_field=CharField()
                                )
                            ).filter(
                                Q(id__range=(low_class, high_class)) &
                                ~Q(new_class_studying='NA')
                            ).values('new_id', 'new_class_studying')

                    # Perform the union operation
                    classstudying = base_query.union(case_query)
                    
                    classmedium = SchoolMediumEntry.objects.filter(
                                Q(isactive=True) & Q(school_key_id=SchlId)
                            ).select_related('medium_instrut').values(
                                'medium_instrut__ID',           
                                'medium_instrut__MEDINSTR_ID',
                                'medium_instrut__MEDINSTR_DESC',
                                'medium_instrut__MEDINSTR_PARENT',
                                'medium_instrut__PREDEFINED',
                                'medium_instrut__VISIBLE_YN',
                                'id',
                                'school_key_id',
                                'medium_instrut',
                                'other_medium',
                                'isactive'
                            )

                    classmedium_ser = SchlMedOfInstSerializer(classmedium, many=True)
                    
                    rtetype = BaseappRteType.objects.all()
                    
                    rtetype_ser = RteSerializer(rtetype, many=True)
                    
                    
                    manage_cate = SchoolNewSchoolDepartment.objects.filter(
                                    schoolnew_basicinfo__school_id=SchlId
                                ).distinct().values('school_mana_id')
      
                    if manage_cate.exists():
                        result = manage_cate.first()  
                        manage_cate_id= result['school_mana_id']
                        
                    if(manage_cate_id == 29):
                        groupname=BaseappGroupCodeCBSE.objects.all()
                        groupname_ser=BaseappGrpCBSESerializer(groupname,many=True)
                    else :
                        groupname=BaseappGroupCode.objects.filter(group_description=1)
                        groupname_ser=BaseappGrpSerializer(groupname,many=True) 
                        
                    bloodgroup = BaseappBloodGroup.objects.all()
                    bloodgroup_ser=BaseappBloodGroupSerializer(bloodgroup,many=True) 
                    
                    manage_cate_list = SchoolBasicInfo.objects.select_related('manage_cate_id').filter(
                                            school_id=SchlId
                                        ).values(
                                            mange_id=F('manage_cate_id__id'),
                                            manage_name=F('manage_cate_id__manage_name')
                                          
                                        )
                                        
                    
                    manage_cate = list(manage_cate_list)
                    
                    manage_ser = [{'id': item['mange_id'], 'manage_name': item['manage_name']} for item in manage_cate]
                    
                    academic=TeacherAcademicQual.objects.all()
                    
                    academic_ser=TeacherAcademicQualSer(academic,many=True)

                else :
                    return JsonResponse({
                    "dataStatus": True,
                    "status": 200,
                    "message":'check Your school Profile',
                    "result" :""
            
                })
                
                    
                result = {"incomes": incomes_ser.data,
                            "religions": religion_ser.data,
                            "launguages": launguages_ser.data,
                            "disadvantages": disadvantages_ser.data,
                            "disabilities": disabilities_ser.data,
                            "schooldist": schooldist_ser.data,
                            "classstudying": list(classstudying),
                            "mediumofinstruction": classmedium_ser.data,
                            "rtetype": rtetype_ser.data,
                            "groupcate":groupname_ser.data,
                            "bloodgroup":bloodgroup_ser.data,
                            "groupcateid":manage_cate_id,
                            "managecateid":manage_ser,
                            "academic":academic_ser.data,
                            "validation_error":"",
                            "lowestclass":low_class,
                            "highclass":high_class
                            
                            }
                

            
                return JsonResponse({
                    "dataStatus": True,
                    "status": 200,
                    "result":result
            
                })
            except Exception as e:
                return JsonResponse({
                    "dataStatus": False,
                    "status": 500,
                    "message": f"{str(e)}"
                })  
                
    def OtpPurpose(self, request):
        
        try:

            result = BaseappOtpPurpose.objects.filter(isactive=1)
            
            serializer = BaseappOtpPurposeSer(result, many=True)
            
            return JsonResponse({
                "dataStatus": True,
                "status": 200,
                "result": serializer.data
            })
        except Exception as e:
            return JsonResponse({
                "dataStatus": False,
                "status": 500,
                "message": f"{str(e)}"
            }) 
            
    
    def schoolWiseClassandSection(self, request):
        try:
            SchlId = request.GET.get('school_id', None)

            result = SchoolNewSectionGroup.objects.filter(
                        school_key_id=SchlId,
                        isactive=True
                    ).select_related('class_id').values(
                        'school_key_id',
                        'class_id',
                        'class_id__class_studying',
                        'section'
                    )
                
            class_sections = defaultdict(list)


            for item in result:
                class_id = item['class_id']
                class_sections[class_id].append(item['section'])

            # Now, create the final list with concatenated sections
            final_result = []
            for class_id, sections in class_sections.items():
                # Concatenate sections and append the result
                final_result.append({
                    'school_key_id': item['school_key_id'],
                    'class_id': class_id,
                    'class_studying': item['class_id__class_studying'],
                    'revalent_section': ','.join(sorted(sections))  # Equivalent to GROUP_CONCAT with ordering
                })
                
                classmedium = SchoolMediumEntry.objects.filter(
                                Q(isactive=True) & Q(school_key_id=SchlId)
                            ).select_related('medium_instrut').values(
                                'medium_instrut__ID',           
                                'medium_instrut__MEDINSTR_ID',
                                'medium_instrut__MEDINSTR_DESC',
                                'medium_instrut__MEDINSTR_PARENT',
                                'medium_instrut__PREDEFINED',
                                'medium_instrut__VISIBLE_YN',
                                'id',
                                'school_key_id',
                                'medium_instrut',
                                'other_medium',
                                'isactive'
                            )

                classmedium_ser = SchlMedOfInstSerializer(classmedium, many=True)
                
                
                        
            return JsonResponse({
                "dataStatus": True,
                "status": 200,
                "result": final_result,
                "medium" :classmedium_ser.data
            })
        except Exception as e:
            return JsonResponse({
                "dataStatus": False,
                "status": 500,
                "message": f"{str(e)}"
            }) 
            
    def classWiseStudentList(self, request):
        try:
            data = json.loads(request.body.decode('utf-8'))
            records = data.get('records', {})
            class_id = records.get('class_id')
            section_id = records.get('section')
            school_id = records.get('school_id')

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
