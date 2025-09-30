from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
# 로그인 폼만 보여주는 것과 로그인이 실행되는 것.
# a 태그는 GET요청
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')

    else:
        form = AuthenticationForm()
        # input 태그만 나열해준다. 이거 무슨 뜻이지?

    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect('articles:index')