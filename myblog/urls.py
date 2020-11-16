from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('new', views.new, name='new'),
  path('new_topic', views.new_topic_form, name='new_topic_form')
]