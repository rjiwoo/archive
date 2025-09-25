from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):

    articles = Article.objects.all()    # DB에 있는 내용을 가져오는 것 => ORM 사용
    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)

def create(request):

    if request.method == 'GET':
        return render(request, 'articles/create.html')
    
    # POST
    # create form에 적어 놓은 저장
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save() # DB에 저장
    return redirect('articles:index')   # 파일명이 아니라 url의 이름을 줘야함.

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article':article,
    }

    return render(request, 'articles/detail.html', context)

def update(request, article_pk):

    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        # article = Article.objects.get(pk=article_pk)
        context = {
            'article':article,
        }

        return render(request, 'articles/update.html', context)
    
    # POST - 수정본을 DB에 저장하고 하고 싶음
    # 1. 원래 데이터를 불러와야함
    # article = Article.objects.get(pk=article_pk)
    
    # 2. 데이터 덮어 씌우기
    article.title = request.POST.get('title')
    article.content= request.POST.get('content')
    article.save() # DB에 저장

    return redirect('articles:detail', article.pk)  # 수정완료된 상세 페이지로 이동하는게 적절해보임

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()

    return redirect('articles:index')