from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import MyBlog
from .forms import MyBlogForm

class IndexView(TemplateView):

  def __init__(self):
    self.params = {
      'title': 'My Blog',
      'msg': 'トピックタイトルの一覧',
      'data': [],
      'form': MyBlogForm(),
      'goto': 'cerate',
    }
  
  def get(self, request):
    data = MyBlog.objects.all()
    self.params['data'] = data
    return render(request, 'myblog/index.html', self.params)

  def post(self, request):
    num = request.POST['id']
    item = MyBlog.objects.get(id=num)
    self.params['data'] = [item]
    self.params['form'] = MyBlogForm(request.POST)
    return render(request, 'myblog/index.html', self.params)

# create model
class NewTopicView(TemplateView):

  def __init__(self):
    self.params = {
      'title': 'New Topic',
      'msg': '新しい記事タイトルを記入',
      'form': MyBlogForm(),
      'goto': 'index',
    }

  def get(self, request):
    return render(request, 'myblog/create.html', self.params)

  def post(self, request):
    obj = MyBlog()
    myblog = MyBlogForm(request.POST, request.FILES, instance=obj)
    myblog.save()
    return redirect(to='/myblog')
