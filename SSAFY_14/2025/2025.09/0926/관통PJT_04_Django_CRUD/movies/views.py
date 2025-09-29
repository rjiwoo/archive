from django.shortcuts import render, redirect
from .models import Movie

# Create your views here.
def index(request):

    movies = Movie.objects.all()

    context = {
        'movies' : movies,
    }

    return render(request, 'movies/index.html', context)


# 영화 등록 페이지로 가기
# 입력된 데이터를 저장하는 create view 함수
# 영화 데이터를 입혁하기 위한 UI를 제공하는 new view 함수를 통합함
def create(request):
    if request.method == 'GET':
        return render(request, 'movies/create.html')
    
    # 영화 저장하기
    movie = Movie()
    movie.title = request.POST.get('title')
    movie.content = request.POST.get('content')
    movie.director = request.POST.get('director')
    movie.save()

    # 메인페이지로 가기
    # return redirect('movies:index')

    # TO DO 
    # 상세 페이지로 리다이렉트
    return redirect('movies:detail', movie.pk)

# 상세 페이지 보여주기
def detail(request, movie_pk):

    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie' : movie,
    }

    return render(request, 'movies/detail.html', context)


# 입력된 데이터를 바탕으로 대상 영화 데이터를 수정하는 update view 함수
# 영화 데이터를 수정하기 위한 UI를 제공하는 edit view함수를 통합함
def update(request, movie_pk):

    movie = Movie.objects.get(pk=movie_pk)
    if request.method == 'GET':
        # article = Article.objects.get(pk=article_pk)
        context = {
            'movie' : movie,
        }

        return render(request, 'movies/update.html', context)
    
    
    # 2. 데이터 덮어 씌우기
    movie.title = request.POST.get('title')
    movie.content= request.POST.get('content')
    movie.director = request.POST.get('director')
    movie.save() # DB에 저장

    return redirect('movies:detail', movie.pk)  # 수정완료된 상세 페이지로 이동하는게 적절해보임

def delete(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    movie.delete()

    return redirect('movies:index')