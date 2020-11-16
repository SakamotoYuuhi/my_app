from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  params = {
    'title': 'myblog',
    'msg': '初の自分のブログです'
  }
  return render(request, 'myblog/index.html', params)