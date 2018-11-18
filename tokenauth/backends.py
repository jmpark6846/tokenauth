from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
User = get_user_model()

class EmailAuthenticationBackend:
    def authenticate(self, request, email=None, password=None):
        if email and password:
            try:
                user = User.objects.get(email=email)
            except:
                return None

            password_valid = check_password(password, user.password)

            if password_valid:
                return user
            else:
                return None
        else:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except:
            return None
