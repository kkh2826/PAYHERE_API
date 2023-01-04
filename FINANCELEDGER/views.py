from rest_framework.views import APIView
from rest_framework.response import Response

import json
import datetime

from django.db.models import Max
from .models import Financeledgerlist
from .serializers import FinanceLedgerSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from PAYHERE.decorator.decorators import JWTAuthorized

'''
    결과값 초기화 함수
'''
def InitResult() :
    result = {
        'success': True,
        'message': ''
    }

    return result

'''
    seq값 구하기
'''
def Get_Seq(stddate, email):

    financeInfo = Financeledgerlist.objects.filter(stddate=stddate, email=email)

    if financeInfo.count() == 0:
        return 1
    else:
        fianceInfo = financeInfo.aggregate(seq=Max('seq')+1)
        seq = fianceInfo['seq']
        return seq

'''
    가계부
'''
class FinanceLedger(APIView):
    # Swagger Description (가계부 입력)
    @swagger_auto_schema(
        operation_id='가계부 입력',
        operation_description='가게부에 입력합니다.',
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'stddate': openapi.Schema(type=openapi.TYPE_STRING, description="날짜"),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description="이메일"),
                'seq': openapi.Schema(type=openapi.TYPE_INTEGER, description="순서"),
                'amount': openapi.Schema(type=openapi.TYPE_INTEGER, description="금액"),
                'paytype': openapi.Schema(type=openapi.TYPE_INTEGER, description="결제방법"),
            },
        ),
        responses={200: openapi.Response(
            description="200 OK",
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'success': openapi.Schema(type=openapi.TYPE_BOOLEAN, description="실행결과"),
                    'message': openapi.Schema(type=openapi.TYPE_STRING, description="실행결과메세지"),
                }
            )
        )}
    )
    @JWTAuthorized
    def post(self, request):

        result = InitResult()

        data = json.loads(request.body)
        print(request.data)
        today = datetime.datetime.now()

        stddate = today.date()
        email = data['email']
        data['seq'] = Get_Seq(stddate=stddate, email=email)

        try:
            financeLedger = FinanceLedgerSerializer(data=data)
            
            if financeLedger.is_valid():
                financeLedger.save()
                result['success'] = True
                result['message'] = "가계부를 입력하였습니다."
            else:
                print('is_valid 에러')
                result['success'] = False
                result['message'] = financeLedger.error_messages
        except:
            print('is_valid 전')
            result['success'] = False
            result['message'] = financeLedger.error_messages
            return Response(result, content_type='application/json')

        return Response(result, content_type='application/json')
        


