from .models import Financeledgerlist, Financeledgerdetail
from rest_framework import serializers




class FinanceLedgerDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Financeledgerdetail
        fields = ['financeledger']


class FinanceLedgerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Financeledgerlist
        fields = ['stddate', 'email', 'seq', 'amount', 'paytype']

    def create(self, validated_data):
        print(validated_data)
        finance = Financeledgerlist.objects.create(**validated_data)
        detail = Financeledgerdetail.objects.create(
            financeledger=finance
        )
        return finance

    

