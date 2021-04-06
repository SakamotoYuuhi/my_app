from django.urls import path
from .views import IndexView, DetailView

urlpatterns = [
  path('', IndexView.as_view(), name='myblog_index'),
  path('<int:page>', IndexView.as_view(), name='myblog_index'),
  path('<str:url>', DetailView.as_view(), name='myblog_detail'),
]