from rest_framework import serializers
from rest_framework.authentication import authenticate

class TokenAuthSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if not user:
                raise serializers.ValidationError('login failed with the credentials')
        else:
            raise serializers.ValidationError('please set email and password')

        attrs['user'] = user
        return attrs