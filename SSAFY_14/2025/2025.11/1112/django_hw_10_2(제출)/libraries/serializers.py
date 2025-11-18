from rest_framework import serializers
from .models import Book

# 전체 도서 목록 확인
class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title',)

# 도서 상세 정보 확인
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'