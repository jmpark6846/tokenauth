from django.contrib.auth.models import Permission
from django.db import models

class CustomPermission(Permission):
    codename = models.CharField('codename', max_length=16)
    parent = models.ForeignKey(Permission, related_name='childs', on_delete=models.CASCADE, verbose_name='부모 권한')

    def __str__(self):
        return self.codename

