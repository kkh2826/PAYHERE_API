from django.db import models

# Create your models here.
class Financeledgerlist(models.Model):
    stddate = models.DateField(db_column='stdDate', primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=50)
    seq = models.IntegerField()
    amount = models.BigIntegerField()
    memo = models.CharField(max_length=50, blank=True, null=True)
    paytype = models.IntegerField(db_column='payType')  # Field name made lowercase.
    createdate = models.DateTimeField(db_column='createDate')  # Field name made lowercase.
    updatedate = models.DateTimeField(db_column='updateDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'financeledgerlist'
        unique_together = (('stddate', 'email', 'seq'),)