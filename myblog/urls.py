from django.conf.urls import url
# from django.urls import path
from .views import IndexView, NewTopicView
from . import views

urlpatterns = [
  url(r'', IndexView.as_view(), name='index'),
  url(r'new', NewTopicView.as_view(), name='new'),
]