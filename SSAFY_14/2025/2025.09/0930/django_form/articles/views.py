from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

# Create your views here.
def index(request):

    articles = Article.objects.all()
    context = {
        'user' : request.user,
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context) # 템플릿의 경로를 줘야함

def create(request):
    # 글 생성. 글 저장하는 것
    if request.method == 'POST':
        form = ArticleForm(request.POST)

        # 유효성 검사 -> 튕기면 오류 메세지까지 담겨서 나옴
        if form.is_valid():
            form.save()
            # article = form.save()   # 잘 저장되면 그 게시글로 갈 것이기 때문에 pk를 받기 위해서 article에 저장하는 것임
            return redirect('articles:index')


    # 게시글 생성하기 위해서 작성할 페이지 줘야함
    else:
        # 폼을 쓸 건데, 정의하고 써야함
        form = ArticleForm()


    # 유효성 검사에 튕겼을 경우, 대비하기 위한 것
    context = {
        'form' : form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)