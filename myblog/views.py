from django.db.models.indexes import Index
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, ListView, DetailView
from django.core.paginator import Paginator

from .models import MyBlog
from .forms import MyBlogForm

class IndexView(ListView):

  queryset = MyBlog.objects.order_by('-id').all()
  template_name = 'myblog/index.html' # デフォルトは モデル名_list.html
  context_object_name = 'datas' # デフォルトはobject_list テンプレート側にデータを送る変数
  paginate_by = 5 # ページネーションする時の1ページあたりの数

# 投稿ページの処理
class CreateView(TemplateView):

  def __init__(self):
    self.params = {
      'title': '投稿ページ',
      'msg': '新しい記事タイトルを記入',
      'form': MyBlogForm(),
    }

  def get(self, request):
    return render(request, 'myblog/create.html', self.params)

  def post(self, request):
    obj = MyBlog()
    myblog = MyBlogForm(request.POST, request.FILES, instance=obj)
    myblog.save()
    return redirect(to='/myblog')

# 詳細ページの処理
class DetailView(DetailView):
  
  model = MyBlog
  template_name = 'myblog/detail.html'
  context_object_name = 'datas' # デフォルトはobject_list テンプレート側にデータを送る変数
