from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  params = {
    'title': 'My Blog',
    'msg': '初の自分のブログです',
    'goto': 'new',
  }
  return render(request, 'myblog/index.html', params)

def new(request):
  params = {
    'title': 'New Topic',
    'msg': '新しい記事タイトルを記入',
    'goto': 'index',
  }
  return render(request, 'myblog/new.html', params)

def new_topic_form(request):
  topic_title = request.POST['topic_title']
  params = {
    'title': 'Topic Title',
    'msg': topic_title,
    'goto': 'index',
  }
  return render(request, 'myblog/new.html', params)
