from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('book',) # 유효성 검사에서 제외시키고, 데이터 조회 시에는 출력

class ReviewListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('content', 'score', )
