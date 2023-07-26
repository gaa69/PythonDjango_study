from django.urls import path
from . import views

urlpatterns = [
    #自分自身（helloプロジェクト）のindex関数を読む
    path('', views.index, name='index'),
]
