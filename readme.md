## 실행 순서
1. 도커 컴포즈 셋업  

        docker-compose run web python manage.py migrate  
        docker-compose run web python manage.py createsuperuser  
        docker-compose up --build  


2. django admin interface 에서 사용자, 권한 생성하기

3. curl, postman으로 API 사용

## 커스텀 권한 모델
    tokenauth/models.py
    
    class CustomPermission(models.Model):
        name: 권한명
        parent: 부모 권한
        ...


    class UserHasPermission(models.Model):
        # 사용자가 권한을 가지고 있음을 나타내는 모델
        user: 사용자
        permission: 권한
        
    
    
    def has_permissions(user, permission_name):
        # 유저가 권한을 갖고 있는지 검사하는 메소드
        

## 뷰

IssueAuthToken `/token/`
- 토큰 발행

  
check_permission `/permission/<permission_name>`
- 권한 확인


## 기타
- 이메일로 유저 인증을 하기 위한 이메일 인증 백엔드 추가 `tokenauth/backends.py`
- 뷰 테스트 코드 추가


## 개발환경
- python 3.6.6
- django 2.1.3
- django rest framework 3.9.0
- docker 18.06.1
- docker-compose 1.23.1
