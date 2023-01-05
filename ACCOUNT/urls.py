from django.urls import path, include
from .views import *

urlpatterns = [
    # 회원가입
    path('registration/', RegisterAccount.as_view()),
    # 로그인
    path('login/', LoginAccount.as_view()),
]