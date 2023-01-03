from django.db import models

# Create your models here.
class Financeledgerlist(models.Model):
    stddate = models.DateField(db_column='stdDate')  # Field name made lowercase.
    email = models.CharField(max_length=50)
    seq = models.IntegerField()
    amount = models.BigIntegerField()
    paytype = models.IntegerField(db_column='payType', default=0)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'financeledgerlist'
        unique_together = (('stddate', 'email', 'seq'),)

class Financeledgerdetail(models.Model):
    financeledger = models.OneToOneField(Financeledgerlist, on_delete=models.CASCADE, related_name='details')
    memo = models.CharField(max_length=1000, blank=True, null=True)
    createdate = models.DateTimeField(db_column='createDate', auto_now_add=True)  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='updateDate', auto_now=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'financeledgerdetail'