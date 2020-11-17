from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import MyBlogModel
from .forms import MyBlogForm

class IndexView(TemplateView):

  def __init__(self):
    self.params = {
      'title': 'My Blog',
      'msg': 'トピックタイトルの一覧',
      'data': [],
      'form': MyBlogForm(),
      'goto': 'new',
    }
  
  def get(self, request):
    data = MyBlogModel.objects.all()
    self.params['data'] = data
    return render(request, 'myblog/index.html', self.params)

  def post(self, request):
    num = request.POST['id']
    item = MyBlogModel.objects.get(id=num)
    self.params['data'] = [item]
    self.params['form'] = MyBlogForm(request.POST)
    return render(request, 'myblog/index.html', self.params)

class NewTopicView(TemplateView):

  def __init__(self):
    self.params = {
      'title': 'New Topic',
      'msg': '新しい記事タイトルを記入',
      'content': '',
      'form': MyBlogForm(),
      'goto': 'index',
    }

  def get(self, request):
    return render(request, 'myblog/new.html', self.params)

  def post(self, request):
    topic_title = request.POST['topic_title']
    content = request.POST['content']
    self.params['msg'] = topic_title
    self.params['content'] = content
    self.params['form'] = MyBlogForm(request.POST)
    return render(request, 'myblog/new.html', self.params)
