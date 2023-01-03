from rest_framework.response import Response
import jwt

from ACCOUNT.models import Userinfo


def JWTAuthorized(func):
    def wrapper(self, request, *args, **kwargs):
        try:
            access_token = request.headers.get('Authorization', None)    

            payload = jwt.decode(access_token, "secretJWTkey", algorithm='HS256')  

            user = Userinfo.objects.get(email=payload['id'])                 
            request.user = user          
                                       
        except jwt.exceptions.DecodeError:                                  
            return Response({'message' : 'INVALID_TOKEN' }, content_type='application/json')
        except user.DoesNotExist:                                        
            return Response({'message' : 'INVALID_USER'}, content_type='application/json')

        return func(self, request, *args, **kwargs)
    return wrapper