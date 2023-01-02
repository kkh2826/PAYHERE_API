from .models import Userinfo
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Userinfo
        fields = ['email', 'password', 'username']