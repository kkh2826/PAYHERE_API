from django.urls import path, include
from .views import *

urlpatterns = [
    # Install한 모듈을 사용하기 위해 URL Route 표시
    path('rest-auth/', include('rest_auth.urls')),

    # 회원가입
    path('registration/', RegisterAccount.as_view()),
    # 로그인
    path('login/', LoginAccount.as_view()),
]