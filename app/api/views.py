from django.http import JsonResponse, HttpResponseBadRequest
from rest_framework.decorators import action
from django.views.decorators.csrf import csrf_exempt
import json
import logging
import jwt
from datetime import datetime, timedelta
from .models import LoginModel
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

logger = logging.getLogger('django')

class LoginViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]
    @csrf_exempt
    @action(detail=False, methods=['post'])
    def login(self, request):
        try:
            if request.method != 'POST':
                return JsonResponse({'error': 'Method not allowed'}, status=405)

            json_data = request.body.decode('utf-8')
            data = json.loads(json_data)
            emis_username = data.get('emis_username')
            logger.debug(f"Received JSON data: {json_data}")

            if len(emis_username) == 10:
                login_details = LoginModel.smclogin(data)
            else:
                login_details = LoginModel.new_login(data, request)

            if login_details['Status']:
                # Your secret key
                secret_key = 'ingDLMRuGe9UKHRNjs7cYckS2yul4lc3'
                # Set token expiration time to 1 hour from now
                exp = datetime.now() + timedelta(hours=1)
                token_data = {
                    'iat': datetime.now(),
                    'exp': exp,
                    **login_details['result']  # Assuming 'result' contains user data
                }
                # Encode the JWT token
                token = jwt.encode(token_data, secret_key, algorithm='HS256')
                encrypted_token = self.encryption_data(token.decode('utf-8'))
                return JsonResponse({
                    "dataStatus": True,
                    "status": 200,
                    "records": {"token": token.decode('utf-8')}
                    # "records": {"token": encrypted_token}  # Uncomment if needed
                })
            else:
                return JsonResponse({
                    "dataStatus": False,
                    "status": 401,
                    "message": login_details['message']
                })

        except Exception as e:
            logger.error(f"An error occurred: {str(e)}")
            return HttpResponseBadRequest(str(e))

    def execute_query(self, query, params):
        logger.debug(f"Executing query: {query} with params: {params}")
        try:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
                result = cursor.fetchall()
            return result
        except Exception as e:
            logger.error(f"SQL error: {str(e)}")
            raise
    
    @action(detail=False, methods=['get'])
    def test(self, request):
        return JsonResponse({
                    "dataStatus": True,
                    "status": 200,
                    "message": "pass"
                })
        
    @staticmethod    
    def encryption_data(string):
        
        letter_to_symbol = {
            'a': '!', 'B': '@', 'c': '#', 'D': '$', 'e': '%',
            'F': '^', 'g': '&', 'i': '?', 'J': '+',
            'k': '=', 'L': '|', 'm': '~', 'N': '/', 'o': '-',
            'P': '_', 'q': '{', 'R': '}', 's': '[', 'T': ']',
            'U': '(', 'v': ')', 'W': '<', 'x': '>', 'Y': ':',
            'z': ';',
            '.': '*',
        }

        result = ''

        for char in string:
            if char.isalpha():
                symbol = letter_to_symbol.get(char, char)
                result += symbol
            else:
                result += char

        return result