### 실행 순서
1. 도커 컴포즈 셋업  

        docker-compose run web python manage.py migrate  
        docker-compose run web python manage.py createsuperuser  
        docker-compose up --build  


2. django admin interface 에서 사용자, 권한 생성하기

3. curl, postman으로 API 사용


