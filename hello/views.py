from django.shortcuts import render
# レスポンスクラス
from django.http import HttpResponse

# ①
def index(request):
    return HttpResponse("Hello Djngo!")

# def index(request):
#     return render(request, 'hello/index.html')