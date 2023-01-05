![header](https://capsule-render.vercel.app/api?type=soft&&color=auto&text=PAYHERE_API)

## 로컬 셋팅 방법
1. 가상환경 셋팅
   * python -m venv venv
   * python -m pip install --upgrade pip
2. 필요한 모듈 설치
   * pip install -r requirements.txt
3. Database 연동
   * python manage.py makemigrations
   * python manage.py migrate

## 구현한 API 리스트
1. 회원가입
2. 로그인
3. 가계부 조회
4. 가계부 입력
5. 가계부 수정
6. 가계부 삭제
7. 가계부 상세내역 조회
8. 가계부 상세내역 삭제


## API 문서화
- Swagger 모듈을 활용한 API 문서화
- <b>http://127.0.0.1:8000/swagger</b> or <b>http://127.0.0.1:8000/redoc</b> (runserver 동작 후 확인 가능)

## 사용한 모듈 (일부)
1. PyJWT - jwt 토큰 발급과 토큰 인증을 위한 모듈
2. MysqlClient - MySQL 데이터베이스 연결을 위한 모듈
3. bcrypt - 회원에 대한 비밀번호를 암호화하기 위한 모듈
4. drf-yasg - Swagger 문서 API 연동을 하기 위한 모듈

## Database 및 Table
- DB 이름 : test
1. userinfo - 사용자 정보 테이블
2. financeledgerlist - 가계부 기본 정보 테이블
3. financeledgerdetail - 가계부 세부 정보 테이블

## 보완점 및 느낀점
1. 모델과의 관계 및 Table 설계에 대한 미숙
2. Django 프로젝트의 SecretKey / JWT Secret Key 등 보안에 필요한 정보 미분리
3. 폴더 Directory 구조에 대한 체계 미확립
4. Pythonic 하지 못한 코드 스타일
5. .gitignore 미확립
6. 테스트코드 미작성
7. 시간부족 및 개발여건 부족으로 인한 완성도 저하 (약 3일간 2시간씩 시간적 할애)
