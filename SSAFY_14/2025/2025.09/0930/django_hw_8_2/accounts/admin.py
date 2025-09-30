from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
# admin site에 대체한 User 모델 등록
admin.site.register(User, UserAdmin)