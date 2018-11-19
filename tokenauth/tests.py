from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from rest_framework.test import APIClient
from .models import CustomPermission, UserHasPermission

def create_user(email, password):
    user = User.objects.create(username=email)
    user.set_password(password)
    user.save()
    return user


class TokenViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = { 'email': 'john@test.com', 'password':'abc123'}
        user = create_user(email='john@test.com', password='abc123')
        self.user = user

    def test_issue_token(self):
        res = self.client.post(reverse('token'), self.user_data)
        self.assertEqual(res.data['success'], True)

        res = self.client.post(reverse('token'), {'email': 'tom@toms.coffee', 'password':'abc123'})
        self.assertEqual(res.data['success'], False)

    def test_check_permission(self):
        self.client.login(username='john@test.com', password='abc123')

        p1 = CustomPermission.objects.create(name='perm1')
        p2 = CustomPermission.objects.create(name='perm2', parent=p1)


        UserHasPermission.objects.create(user=self.user, permission=p1)

        res = self.client.get(reverse('check_permission', kwargs={'permission_name':'perm1'}))
        self.assertEqual(res.data['success'], True)

        res = self.client.get(reverse('check_permission', kwargs={'permission_name': 'perm2'}))
        self.assertEqual(res.data['success'], True)