from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  params = {
    'title': 'myblog',
    'msg': '初の自分のブログです',
    'goto': 'new',
  }
  return render(request, 'myblog/index.html', params)

def new(request):
  params = {
    'title': 'new topic',
    'msg': '新しい記事を作成できます',
    'goto': 'index',
  }
  return render(request, 'myblog/new.html', params)
