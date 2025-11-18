from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from .models import Book
from .serializers import BookListSerializer, BookSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def book_list(request):
    # 도서 목록 조회
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)
    
    # 도서 생성
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 저장 성공 응답
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 저장 실패 응답
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'DELETE'])
def book_detail(request, book_pk):
    # 도서 상세 정보 조회
    book = Book.objects.get(pk=book_pk)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    # 도서 삭제
    elif request.method == 'DELETE':
        isbn = book.isbn
        title = book.title
        book.delete()
        data = {
            'delete' : f'도서 고유번호 {isbn}번의 {title}을 삭제하였습니다.'
        }
        return Response(data, status=status.HTTP_200_OK)


