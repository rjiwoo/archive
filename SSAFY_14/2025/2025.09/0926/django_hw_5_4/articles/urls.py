from django.urls import path
from . import views


app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/detail/', views.detail, name='detail'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
]

