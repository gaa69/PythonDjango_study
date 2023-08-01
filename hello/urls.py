from django.urls import path
from . import views

urlpatterns = [
    #②「''」自分自身（helloプロジェクト）のindex関数を読む
    # nameはviews.indexに名前をつけている
    path('', views.index, name='index'),
]