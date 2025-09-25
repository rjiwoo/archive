from django.shortcuts import render, redirect
from .models import Article 

# Create your views here.

# 전체 게시글 조회(1) 후 메인 페이지 응답(2)
def index(request):
    # 1. DB에 전체 게시글을 조회
    articles = Article.objects.all()

    # 2. 전체 게시글 목록을 템플릿과 함께 응답
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

# 게시글 상세 페이지를 응답하는 함수(detail이라는 이름의 함수)
# 1. 몇 번 게시글인지 DB에 조회
# 2. 조회한 상세 게시글 데이터를 템플릿과 함께 응답
def detail(request, pk):
    # 1. 단일 게시글 조회
    # queryset API method ==> get() 예외사항) 없을 때 or 여러개 --> 유일한 식별자를 조회할 때 get()을 써야하는구나
    # Article.objects.get(id=pk)
    article = Article.objects.get(pk=pk) # 앞의 pk는 Article의 컬럼인 pk(=id), 뒤의 pk는 변수로 입력 받은 pk

    # 2. 단일 게시글 데이터와 템플릿을 응답
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

# 사용자가 게시글 생성을 위한 작성 페이지를 응답하는 함수
def new(request):
    return render(request, 'articles/new.html')

# 1. 사용자로부터 입력 받은 데이터를 추출
# 2. 추출한 데이터를 DB에 저장
# 3. 저장이 완료되었다는 페이지를 응답
def create(request):
    # 1. 
    title = request.POST.get('title') # 가져와야하는 key 값은 html에서 input의 name
    content = request.POST.get('content')

    # 2. 추출한 데이터를 DB에 저장해야하는데, 저장 방식이 3가지가 있었음
    # --> 데이터를 추가하기 전에 유효성 검사를 해야하기 때문에 저장 전에 끊어줘야하기 때문에 3번은 패스. 
    # 2.1 인스턴스 생성 후 속성 할당 및 저장
    # article = Article()
    # article.title = title # 오른쪽 title은 위에 있는 title 변수명임. 
    # article.content = content
    # article.save()

    # 2.2 인스턴스 생성 시 속성 할당 후 저장
    article = Article(title=title, content=content)
    article.save()

    # # 3.3 create() 메서드를 통한 인스턴스 생성 및 즉시 저장
    # Article.objects.create(title=title, content=content)

    # 클라이언트의 요청 사항
    # 1. 게시글 생성해줘! (POST) -> 페이지 요청이 아니라서 render()가 아님. render()는 페이지를 응답하는 것이기 때문에
    #                               게시글 저장 후 페이지를 응답하는 것은 POST 요청에 대한 적절한 응답이 아님
    #                               사용자를 적절한 기존 페이지로 보내야 함 (이건 사람의 입장)
    #                               실제로 서버가 클라이언트를 직접 다른 페이지로 보내는 것이 아닌 클라이언트가 GET 요청을 한번 더 보내도록 응답하는 것
    #                            -> redirect() : 클라이언트가 인자에 작성된 주소로 다시 요청을 보내도록 하는 함수
    # 2. 게시글 완료 페이지 줘! (GET) -> render()
    # return render(request, 'articles/create.html')

    # 클라이언트한테 새로운 주소로 요청을 보내게끔 시켜야 함
    return redirect('articles:detail', article.pk) # 지금 막 생성된 article의 pk로 이동하겠다. 방금 만들어진 페이지로 이동할 것이다. 



def delete(request, pk):
    # 1. 어떤 게시글을 삭제할 건지 조회
    article = Article.objects.get(pk=pk)

    # 2. 조회한 게시글을 삭제
    article.delete()

    # 3. 메인페이지로 리다이렉트
    return redirect('articles:index')