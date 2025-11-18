from django.shortcuts import render, redirect
from .models import Book
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm

# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'libraries/index.html', context)

def detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book,
    }
    return render(request, 'libraries/detail.html', context)


@login_required
def review_create(request, pk):
    book = Book.objects.get(pk=pk)
    review_form = ReviewForm(request.POST)
    if review_form.is_valid():
        review = review_form.save(commit=False)
        review.book = book
        review.user = request.user
        review.save()
        return redirect('libraries:detail', book.pk)
    context = {
        'book' : book,
        'review_form' : review_form,
    }
    return render(request, 'libraries/detail.html', context)