import hashlib
import os
import re
from django.db import connection

class LoginModel:
    @classmethod        
    def new_login(cls, records, request):
        emis_username = records.get('emis_username')
        emis_password = records.get('emis_password')
        length = len(emis_username)
        result = {}

        if length == 7:
            sql_query = """
                SELECT esp.user_type, esp.user_type1 
                FROM emis_login el 
                JOIN external_user_profile esp ON esp.user_id = el.user_id 
                WHERE el.user_id = %s
            """
        elif length == 11:
            sql_query = """
                SELECT 1 AS user_type, 0 AS user_type1 
                FROM emis_login el 
                JOIN schoolnew_basicinfo us ON us.udise_code = el.user_id 
                WHERE el.user_id = %s
            """
        else:
            sql_query = """
                SELECT us.user_type, us.user_type1 
                FROM emis_login el 
                JOIN udise_staffreg us ON us.teacher_id = el.user_id 
                WHERE el.user_id = %s AND us.archive IN (1, 3)
            """

        with connection.cursor() as cursor:
            cursor.execute(sql_query, [emis_username])
            row = cursor.fetchone()

            if not row:
                return {
                    'Status': False,
                    'message': 'User not found in the database'
                }

            emis_usertype = row[0]
            emis_usertype1 = row[1]

            if length == 7:
                mht_sel = ""
                mht_join = ""
                if emis_usertype == 27 and emis_usertype1 == 6:
                    mht_sel = 'aim.block_id as mht_block_id,'
                    mht_join = 'LEFT JOIN awc_index_mhtmap aim ON aim.user_id = el.user_id'

                sql_query = f"""
                    SELECT eup.user_id as emis_username, eup.name, eup.phone, eup.email, eup.email2, eup.designation,
                        eup.user_type as emis_usertype, {mht_sel} 
                        eup.user_type1 as emis_usertype1, eup.department, IF(eup.status=1, 'Active', 'Inactive') as status,
                        el.password as emis_password, IF(eup.block_id>0 and eup.block_id is not null, eup.block_id, eup.district_id) as user_id, 
                        0 as temp_login, eup.block_id, eup.district_id
                    FROM external_user_profile eup 
                    JOIN emis_login el ON el.user_id = eup.user_id 
                    {mht_join}
                    WHERE eup.user_id = %s
                """
         
                cursor.execute(sql_query, [emis_username])
                row = cursor.fetchone()

            elif length == 8 or length == 6:
                sql_query = """
                    SELECT us.user_type, us.user_type1, us.user_id as emis_username,
                    emis_login.password as emis_password, IF(us.archive=1 or us.archive=3 
                    or us.temp_login=1, 'Active', 'Inactive') as status, us.teacher_name,
                    us.udise_code, '' as district_id, '' as block_id
                    FROM udise_staffreg us
                    LEFT JOIN emis_login ON us.teacher_id = emis_login.user_id
                    WHERE emis_login.user_id = %s and us.archive in (1, 3)
                """
                cursor.execute(sql_query, [emis_username])
                row = cursor.fetchone()

            elif length == 11:
                sql_query = """
                    SELECT emis_login.user_id as emis_username, sch.school_id as emis_user_id, 1 as emis_usertype,
                    0 as emis_usertype1, emis_login.password as emis_password, IF(sch.curr_stat=1, 'Active', 'Inactive') as status,
                    sch.school_name as teacher_name, sch.udise_code, 0 as temp_login, '' as district_id, '' as block_id
                    FROM schoolnew_basicinfo sch
                    LEFT JOIN emis_login ON sch.udise_code = emis_login.user_id
                    WHERE emis_login.user_id = %s
                """
                cursor.execute(sql_query, [emis_username])
                row = cursor.fetchone()

            if not row:
                return {
                    'Status': False,
                    'message': 'User details not found in the database'
                }

            result = {desc[0]: value for desc, value in zip(cursor.description, row)}

            mod_cond = []
            if 'emis_usertype' in result:
                mod_cond.append(f"id='{result['emis_usertype']}'")
            if 'emis_usertype1' in result:
                mod_cond.append(f"user_type1='{result['emis_usertype1']}'")

            # Joining the conditions with 'AND'
            para = " AND ".join(mod_cond) if mod_cond else ""
      
            # Executing the SQL query with the dynamic conditions
            cursor.execute(f"SELECT * FROM user_category WHERE {para}")
            row = cursor.fetchone()
  
            if not row:
                return {
                    'Status': False,
                    'message': 'User category not found in the database'
                }

            mod1 = row[6]
            mod2 = row[7]

            cursor.execute(f"SELECT * FROM user_module_inc_exc WHERE user_id=%s AND is_active=1 ORDER BY id DESC LIMIT 1", [emis_username])
            inc_ex_rs = cursor.fetchone()

            if inc_ex_rs:
                inc_ex = inc_ex_rs
                app_modules = mod1.split(',')
                if inc_ex[2] != '':
                    app_modules += inc_ex[2].split(',')

                for m in inc_ex[2].split(','):
                    if m in app_modules:
                        app_modules.remove(m)

                result['mod1'] = ','.join(app_modules)

                web_modules = mod2.split(',')
                if inc_ex[3] != '':
                    web_modules += inc_ex[3].split(',')

                for m in inc_ex[3].split(','):
                    if m in web_modules:
                        web_modules.remove(m)

                result['mod2'] = ','.join(web_modules)

            if result['emis_usertype'] == '14' or result['emis_usertype'] == '8':
                if result['school_key_id'] < '90000':
                    schl_id = result['school_key_id']
                    sql = f"SELECT udise_code FROM students_school_child_count WHERE school_id = '{schl_id}'"
                    cursor.execute(sql)
                    school = cursor.fetchone()
                    if school:
                        result['rsa_school_id'] = school['udise_code']
                elif result['school_key_id'] > '90000':
                    result['rsa_school_id'] = result['school_key_id']

            hashed_password = hashlib.md5(emis_password.encode()).hexdigest()

            if result and result['status'] == 'Active':
                if result['emis_password'] == hashed_password:
                    del result['emis_password']
                    ip_address = cls.get_ip_address(request)  # Get IP address from request
                    user_agent = request.META.get('HTTP_USER_AGENT', '')
                    update_log = {
                        'device': cls.detect_device(user_agent),
                        'ip_address': cls.get_ip_address(request),
                        'device_details': user_agent,
                        'type': 'in',
                        'user_id': emis_username
                    }
                    # cls.newlogin_record_log(update_log)

                    return {
                        'Status': True,
                        'message': '',
                        'result': result
                    }
                else:
                    return {
                        'Status': False,
                        'message': 'Password Mismatch'
                    }
            else:
                return {
                    'Status': False,
                    'message': 'Your Account is Inactive. Please Contact tnemiscel@gmail.com'
                }
    

    @staticmethod
    def get_ip_address(request):
        ip = (
            request.environ.get('HTTP_CLIENT_IP') or
            request.environ.get('HTTP_X_FORWARDED_FOR') or
            request.environ.get('HTTP_X_FORWARDED') or
            request.environ.get('HTTP_FORWARDED_FOR') or
            request.environ.get('HTTP_FORWARDED') or
            request.environ.get('REMOTE_ADDR')
        )
        return ip
    
    def detect_device(user_agent):
        device = '' 
        if re.match(r'(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|iris|kindle|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino', user_agent) or \
                re.match(r'1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-', user_agent[:4]):
            device = 'Mobile'
        else:
            device = 'Desktop'
        return device
    
    @staticmethod
    def newlogin_record_log(update_log):
        
        device=update_log['device']
        ip_address=update_log['ip_address']
        device_details=update_log['device_details']
        user_id=update_log['user_id']
        
        sql_query = """
            INSERT INTO emis_login_log (user_id,device, ip_address, device_details,type)
            VALUES (%s, %s, %s, %s, %s)
        """
        
        # Execute the raw SQL query
        with connection.cursor() as cursor:
            cursor.execute(sql_query, [user_id,device, ip_address, device_details, 'in'])
            
            connection.commit()
            
            return 1


    

                
    
    
