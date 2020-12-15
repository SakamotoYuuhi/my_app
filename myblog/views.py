from django.urls import path, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import MyBlog
from .forms import MyBlogForm

class IndexView(ListView):
  queryset = MyBlog.objects.order_by('-id').all()
  template_name = 'myblog/index.html' # デフォルトは モデル名_list.html
  context_object_name = 'datas' # デフォルトはobject_list テンプレート側にデータを送る変数
  paginate_by = 5 # ページネーションする時の1ページあたりの数

# 詳細ページの処理
class DetailView(DetailView): 
  model = MyBlog
  template_name = 'myblog/detail.html'
  context_object_name = 'datas' # デフォルトはobject_list テンプレート側にデータを送る変数

# 投稿ページの処理
class CreateView(CreateView):
  template_name = 'myblog/create.html'
  form_class = MyBlogForm
  success_url = '/myblog/'

  # このメソッドは、有効なフォームデータがPOSTされたときに呼び出される
  def form_valid(self, form):
    path
    return super().form_valid(form)

# 編集ページの処理
class EditView(UpdateView):
  model = MyBlog
  template_name = 'myblog/edit.html'
  form_class = MyBlogForm
  context_object_name = 'datas' # デフォルトはobject_list テンプレート側にデータを送る変数

  # このメソッドは、有効なフォームデータがPOSTされたときに呼び出される
  def form_valid(self, form):
    path
    return super().form_valid(form)

# 投稿されたデータを処理
class DeleteView(DeleteView):
  model = MyBlog
  context_object_name = 'datas' # デフォルトはobject_list テンプレート側にデータを送る変数
  success_url = reverse_lazy('index')