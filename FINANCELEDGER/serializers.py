from .models import Financeledgerlist, Financeledgerdetail
from rest_framework import serializers
import datetime




class FinanceLedgerDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Financeledgerdetail
        fields = [ 'memo', 'createdate', 'updatedate']



class FinanceLedgerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Financeledgerlist
        fields = ['stddate', 'email', 'seq', 'amount', 'paytype']

    def create(self, validated_data):
        finance = Financeledgerlist.objects.create(**validated_data)
        detail = Financeledgerdetail.objects.create(
            financeledger=finance
        )
        return finance

    # def update(self, instance, validated_data):
    #     print(validated_data)
    #     print('여기 들어오니')
    #     print(instance)
    #     instance.updatedate = datetime.datetime.now()
    #     instance.save()
    #     detail = Financeledgerdetail.objects.update(
    #         financeledger=instance
    #     )
    #     return instance

    

