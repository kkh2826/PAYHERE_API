from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

import json

from .models import Userinfo
from .serializers import UserSerializer

# Create your views here.

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

'''
    결과값 초기화 함수
'''
def InitResult() :
    result = {
        'user': None,
        'token': '',
        'success': True,
        'message': ''
    }

    return result


'''
    회원가입
'''
class RegisterAccount(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        result = InitResult()

        data = json.loads(request.body)

        return Response(result, content_type='application/json')
