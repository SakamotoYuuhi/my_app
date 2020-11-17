from django.urls import path
from .views import IndexView, NewTopicView
# from . import views

urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('new', NewTopicView.as_view(), name='new'),
]