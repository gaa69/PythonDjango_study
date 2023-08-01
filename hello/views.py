from django.shortcuts import render
# レスポンスクラス
from django.http import HttpResponse

def index(request):

    # ①パラメータ表示方法
    # GET['msg']の中に値があるかチェック
    if 'msg' in request.GET:
        msg = request.GET['msg']
        return HttpResponse('パラメータを表示 「'+msg+'」')
    else:
        result = 'パラメータはないよ'

    return HttpResponse(result)