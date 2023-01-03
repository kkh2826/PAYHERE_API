from .models import Financeledgerlist, Financeledgerdetail
from rest_framework import serializers


class FinanceLedgerDetailSerializer(serializers.ModelSerializer):

    detail = serializers.PrimaryKeyRelatedField(queryset=Financeledgerlist.objects.all())

    class Meta:
        model = Financeledgerdetail

class FinanceLedgerSerializer(serializers.ModelSerializer):

    #detail = FinanceLedgerDetailSerializer()

    class Meta:
        model = Financeledgerlist
        fields = ['stddate', 'email', 'seq', 'amount', 'paytype']

    # def create(self, validated_data):
    #     #detail = validated_data.pop('detail', None)
    #     item = Financeledgerlist(**validated_data)
    #     item.save()
    #     Financeledgerdetail.objects.create(financeledger=item)

    #     return item

