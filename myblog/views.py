from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .forms import MyBlogForm

def index(request):
  params = {
    'title': 'My Blog',
    'msg': '初の自分のブログです',
    'goto': 'new',
  }
  return render(request, 'myblog/index.html', params)

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
