from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

import json
import bcrypt

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
        'email': None,
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

        data['password'] = bcrypt.hashpw(data['password'].encode("UTF-8"), bcrypt.gensalt()).decode("UTF-8")
        email = data['email']

        try:
            if Userinfo.objects.filter(email=email).exists():
                result['success'] = False
                result['message'] = "이미 존재하고 있는 이메일 입니다."
                return Response(result, content_type='application/json')
           
            userinfo = UserSerializer(data=data)    
            
            if userinfo.is_valid():
                userinfo.save()
                result['email'] = email
                result['success'] = True
                result['message'] = "정상적으로 회원가입 되었습니다."
        except:
            result['success'] = False
            result['message'] = userinfo.errors
            return Response(result, content_type='application/json')

        return Response(result, content_type='application/json')


'''
    로그인
'''
class LoginAccount(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        result = InitResult()
        token = ''

        data = json.loads(request.body)

        email = data['email']
        password = data['password']

        user = Userinfo.objects.get(
            email = email
        )

        if user is None:
            result['success'] = False
            result['message'] = "존재하지 않는 이메일입니다."
        else:
            if bcrypt.checkpw(password.encode("UTF-8"), user.password.encode("UTF-8")):
                try:
                    payload = JWT_PAYLOAD_HANDLER(user)
                    token = JWT_ENCODE_HANDLER(payload)
                except:
                    result['success'] = False
                    result['message'] = "토큰의 정보를 가져오지 못했습니다."
                    
                result['email'] = email
                result['token'] = token        
            else:
                result['success'] = False
                result['message'] = "비밀번호를 확인해주세요."

        return Response(result, content_type='application/json')