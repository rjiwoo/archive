from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

# 전체 유저 목록 확인
def index(request):
    users = User.objects.all()
    context = {
        'users' : users,
    }
    return render(request, 'accounts/index.html', context)

# 로그인 기능
def login(request):
    # 로그인 폼 제출
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('accounts:index') # 로그인 성공하면 index 페이지 가야함. 

    # GET 요청일 때, 로그인 페이지를 응답
    # GET 요청은 <a> 태그
    form = AuthenticationForm()
    context = {
        'form' : form,
    }
        
    return render(request, 'accounts/login.html', context)


# 로그아웃
def logout(request):
    auth_logout(request)
    return redirect('accounts:index')