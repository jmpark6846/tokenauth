from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import TokenAuthSerializer
from .models import has_permissions

class IssueAuthToken(ObtainAuthToken):
    serializer_class = TokenAuthSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})

        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError:
            return Response({'success':False, 'message': '로그인에 실패했습니다. 아이디와 비밀번호를 확인하세요.'})

        user = serializer.validated_data['user']


        token, created = Token.objects.get_or_create(user=user)
        print(token, created)
        return Response({ 'success': True, 'message':'성공', 'token:':token.key })


@api_view(['GET'])
def check_permission(request, permission_name):
    if not permission_name:
        return Response({ 'success': False, 'message': 'permission_name이 필요합니다.'})

    result = has_permissions(request.user, permission_name)
    return Response({ 'success':True, 'message':result, 'permission_name': permission_name})
