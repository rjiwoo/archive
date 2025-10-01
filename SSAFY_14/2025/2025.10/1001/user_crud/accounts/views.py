from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash

# Create your views here.
# 회원가입
def signup(request):
    if request.method == "POST":
        # 1. form 기반 데이터 받기
        form = CustomUserCreationForm(request.POST)
        # 2. form 데이터 유효성 검사
        if form.is_valid():
            # 3. 유효하다면 가입 처리 > DB 저장
            user = form.save()  # form.save()를 하면 저장한 객체를 뱉어내?

            # 혹시 로그인 하고 싶다면 하기
            auth_login(request, user)

            # 4. 가입 처리 완료 후 메인 페이지로 이동
            return redirect('articles:index')
    
    else:
        form = CustomUserCreationForm() # model Form -> DB 
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)

# 로그인
def login(request):
    if request.method == "POST":
        # 1. form 기반 데이터 받기
        form = AuthenticationForm(request, request.POST)    # 인증관련은 첫 인자가 request
        # 2. form 데이터 유효성 검사
        if form.is_valid():
            # 3. 로그인 완료 후 메인 페이지로 이동(세션 저장 = auth_login)
            auth_login(request, form.get_user())
            return redirect('articles:index')
    
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

# 로그아웃
def logout(request):
    auth_logout(request)    # 세션만 지우면 됨
    return redirect('articles:index')

# TO DO : 회원 탈퇴하면 로그아웃도 되게 처리하기
# 삭제가 안되었는데, 로그아웃 되면 안되니까 
# 회원 정보 삭제 먼저 하고 로그아웃
# 회원탈퇴
def delete(request):
    request.user.delete()   # 회원 정보 DB에서 삭제
    auth_logout(request)    # 로그아웃
    return redirect('articles:index')


# 회원정보수정
def update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            # 유효하다면 수정해서 > DB 저장
            form.save()  
        return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)

# 비밀번호 수정
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/password.html', context)