from django.conf.urls import url
from django.urls import path
from .views import NewTopicView
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  url(r'new', NewTopicView.as_view(), name='new'),
]