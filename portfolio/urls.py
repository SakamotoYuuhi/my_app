from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
# from .views import IndexView, CreateView, DetailView, EditView, DeleteView
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  # path('<int:page>', IndexView.as_view(), name='index'),
  # path('detail/<int:pk>', DetailView.as_view(), name='detail'),
  # path('create', CreateView.as_view(), name='create'),
  # path('edit/<int:pk>', EditView.as_view(), name='edit'),
  # path('delete/<int:pk>', DeleteView.as_view(), name='delete'),
  # path('login', LoginView.as_view(template_name='myblog/login.html'), name='login'),
  # path('logout', LogoutView.as_view(template_name='myblog/logout.html'), name='logout'),
]