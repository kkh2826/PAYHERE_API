from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

import json
import datetime

from django.db.models import Max
from .models import Financeledgerlist, Financeledgerdetail
from .serializers import FinanceLedgerSerializer, FinanceLedgerDetailSerializer

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from PAYHERE.decorator.decorators import JWTAuthorized

'''
    Swagger에서 공통적으로 Authorization(Header)에 적용시켜야 하는 JWT Token 정보
'''
parameter_token = openapi.Parameter(
    "Authorization",
    openapi.IN_HEADER,
    description="JWT Token",
    type=openapi.TYPE_STRING
)

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
        manual_parameters=[parameter_token],
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

    
    # Swagger Description (가계부 조회)
    email = openapi.Parameter('email', openapi.IN_QUERY, description="이메일", type=openapi.TYPE_STRING, required=True)
    stddate = openapi.Parameter('stddate', openapi.IN_QUERY, description="기준일", type=openapi.TYPE_STRING, required=False)
    @swagger_auto_schema(
        operation_id='가계부 조회',
        operation_description='로그인된 회원의 가계부를 조회합니다.',
        manual_parameters=[parameter_token, email, stddate]
    )
    @JWTAuthorized
    def get(self, request):
        queryset = Financeledgerlist.objects.all()
        
        if request.query_params:
            email = request.query_params.get('email')
            stddate = request.query_params.get('stddate', None)
            
            if stddate is None:
                queryset = queryset.filter(email=email, stddate=datetime.datetime.now().date())
            else:
                queryset = queryset.filter(email=email, stddate=stddate)
        
        serializer = FinanceLedgerSerializer(queryset, many=True)

        return Response(serializer.data, content_type='application/json')


    @JWTAuthorized
    def put(self, request):

        result = InitResult()

        data = json.loads(request.body)

        stddate = data['stddate']
        email = data['email']
        seq = data['seq']

        finance = Financeledgerlist.objects.get(
            stddate=stddate,
            email=email,
            seq=seq
        )
        detail = Financeledgerdetail.objects.get(financeledger_id=finance.pk)
        
        try:
            serializer = FinanceLedgerSerializer(finance, data=data)
            if serializer.is_valid():
                serializer.save()
                detail.save(
                    update_fields=['updatedate']
                )
  
                result['success'] = True
                result['message'] = "가게부 정보를 수정하였습니다."
                
        except:
            result['success'] = False
            result['message'] = serializer.error_messages

        return Response(result, content_type='application/json')

'''
    가계부 Detail
'''
class FinanceLedgerDetail(APIView):
    # Swagger Description (가계부 세부사항 조회)
    @swagger_auto_schema(
        operation_id='가계부 세부사항 조회',
        operation_description='가게부 입력된 항목에 대해 세부사항을 보여줍니다.',
        manual_parameters=[parameter_token],
    )
    @JWTAuthorized
    def get(self, request, pk):

        detail = Financeledgerdetail.objects.get(financeledger_id=pk)
        serializer = FinanceLedgerDetailSerializer(detail)

        return Response(serializer.data, content_type='application/json')


    # Swagger Description (가계부 세부사항 수정)
    @swagger_auto_schema(
        operation_id='가계부 세부사항 수정',
        operation_description='가게부 입력된 항목에 대해 세부사항을 수정합니다.',
        manual_parameters=[parameter_token],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'memo': openapi.Schema(type=openapi.TYPE_STRING, description="메모"),
                'createdate': openapi.Schema(type=openapi.TYPE_STRING, description="최초생성시간"),
                'updatedate': openapi.Schema(type=openapi.TYPE_INTEGER, description="수정된시간"),
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
    def put(self, request, pk):

        result = InitResult()

        detail = Financeledgerdetail.objects.get(financeledger_id=pk)
        data = json.loads(request.body)
        
        try:
            serializer = FinanceLedgerDetailSerializer(detail, data=data)
            if serializer.is_valid():
                serializer.save()
                result['success'] = True
                result['message'] = "가계부 세부사항을 수정하였습니다."
            else:
                result['success'] = False
                result['message'] = serializer.error_messages
        except:
            result['success'] = False
            result['message'] = serializer.error_messages
        

        return Response(result, content_type='application/json')