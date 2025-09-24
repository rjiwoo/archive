from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    
    articles = Article.objects.all() # ORM 쓰는 중
    print(articles.query)
    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)

def dummy_create(request):

    for i in range(1,11):
        article = Article(title=f'{i}번 게시글', content=f'{i}번 내용')
        article.save()

    return redirect('articles:index')