from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User

User = get_user_model()

class EmailAuthenticationBackend:
    def authenticate(self, request, email=None, password=None):
        '''
        django default User 모델은 username이 pk이므로
        username 필드에 email을 저장하거나 email이 pk인 custom user 모델을 만들어야한다.
        여기선 전자를 선택.
        :return: 인증 성공 시 유저 인스턴스, 실패 시 None
        '''

        if email and password:
            try:
                user = User.objects.get(username=email)
            except User.DoesNotExist:
                return None

            password_valid = check_password(password, user.password)

            if password_valid:
                return user

            return None
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
