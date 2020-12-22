from django.urls import path
from .views import IndexView, CreateView, DetailView, EditView, DeleteView

urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('<int:page>', IndexView.as_view(), name='index'),
  path('detail/<int:pk>', DetailView.as_view(), name='detail'),
  path('create', CreateView.as_view(), name='create'),
  path('edit/<int:pk>', EditView.as_view(), name='edit'),
  path('delete/<int:pk>', DeleteView.as_view(), name='delete'),
]