from django.contrib import admin
from .models import CustomPermission, UserHasPermission

# Register your models here.
admin.site.register(CustomPermission)
admin.site.register(UserHasPermission)