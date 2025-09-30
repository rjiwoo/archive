from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm

# Create your views here.
def index(request):
    reservations = Reservation.objects.all()
    context = {
        'reservations': reservations
    }
    return render(request, 'reservations/index.html', context)

# 작성한 ModelForm을 'reservations/new.html'에게 넘겨준다.
def new(request):
    form = ReservationForm()
    context = {
        'form' : form,
    }
    return render(request, 'reservations/new.html', context)

# ModelForm을 사용하여 넘겨받은 데이터를 담는다.
def create(request):
    form = ReservationForm(request.POST)

    # 정상적인 데이터라면 데이터를 생성 후 reservations:index' 경로로 redirect
    if form.is_valid():
        form.save()
        return redirect('reservations:index')
    
    
    # 유효성 검사를 통과하지 못하면? 해당 페이지를 다시 응답 + 에러 메세지를 포함
    context = {
        'form' : form,
    }
    return render(request, 'reservations/new.html', context)
