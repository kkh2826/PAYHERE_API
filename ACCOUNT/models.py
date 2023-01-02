from django.db import models

# Create your models here.
class Userinfo(models.Model):
    email = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userinfo'