from rest_framework import serializers
from .models import Book, Review


class BookListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('title', )


class BookSerializer(serializers.ModelSerializer):
    class ReviewDetailSerializer(serializers.ModelSerializer):
        class Meta:
            model = Review
            fields = ('content', 'score')
    review_set = ReviewDetailSerializer(many=True, read_only=True)

    review_count = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'
    
    def get_review_count(self, obj):
        return obj.review_count

class ReviewListSerializer(serializers.ModelSerializer):
    class BookISBNSerializer(serializers.ModelSerializer):
        class Meta:
            model = Book
            fields = ('isbn',)
    book = BookISBNSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ('book', 'content', 'score',)

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields=('book',)
