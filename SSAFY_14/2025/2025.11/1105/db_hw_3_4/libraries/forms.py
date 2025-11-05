from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    # Python의 Inner class라는 문법과 무관.
    class Meta:
        model = Book
        fields = ['title', 'description', 'adult', 'price']

