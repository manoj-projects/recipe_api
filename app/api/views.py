from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import MobileModel
import jwt
from django.conf import settings
import sys

@csrf_exempt
def login(request):
    if request.method == 'POST':
        json_data = request.body.decode('utf-8')
        data = json.loads(json_data)
        records = data.get('records')
        emis_username = records.get('emis_username')
        emis_password = records.get('emis_password')
        
        # Retrieve login details from MobileModel (you need to implement this method)
        login_details = MobileModel.login(emis_username)
        
        if login_details:
            # Create payload for JWT
            payload = {
                'username': emis_username,
            }
            print("Payload:", payload)
            # print("Secret Key:", settings.JWT_SECRET_KEY)
            
            jwt_secret_key = settings.JWT_AUTH['JWT_SECRET_KEY']
          
      
            token = jwt.encode(payload, settings.jwt_secret_key, algorithm='HS256')
  
            
            # Return the token in the JSON response
            return JsonResponse({'token': token})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
