from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }

    return render(request, 'articles/index.html', context)


# 게시글 생성을 위한 form을 보여준다
def new(request):
    return render(request, 'articles/new.html')


# 데이터 저장 후 메인페이지로 이동
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    article = Article(title=title, content=content)
    article.save()

    return redirect('articles:index')