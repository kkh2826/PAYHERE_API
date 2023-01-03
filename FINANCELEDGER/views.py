from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response

import json
import datetime

from django.db.models import Max
from .models import Financeledgerlist
from .serializers import FinanceLedgerSerializer


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

    if financeInfo is None:
        return 1
    else:
        return financeInfo.aggregate(Max('seq'))

'''
    가계부
'''
class FinanceLedger(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [JSONWebTokenAuthentication]

    def post(self, request):

        result = InitResult()

        data = json.loads(request.body)

        today = datetime.datetime.now()

        stddate = today.date()
        email = data['email']
        seq = Get_Seq(stddate=stddate, email=email)
        amount = data['amount']
        paytype = 0

        try:
            financeLedger = FinanceLedgerSerializer(data=data)
            if financeLedger.is_valid():
                financeLedger.save()
        except:
            return Response(result, content_type='application/json')


