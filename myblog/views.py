from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.paginator import Paginator

from .models import MyBlog
from .forms import MyBlogForm

class IndexView(TemplateView):

  def __init__(self):
    self.data = MyBlog.objects.reverse().all()
    self.paginator = Paginator(self.data, 5)
    self.params = {
      'title': 'My Blog',
      'msg': 'トピックタイトルの一覧',
    }
  
  def get(self, request, page=1):
    self.params['data'] = self.paginator.get_page(page)
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
