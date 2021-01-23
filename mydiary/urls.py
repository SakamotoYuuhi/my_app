from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import IndexView, CreateView, DetailView, EditView, DeleteView

urlpatterns = [
  path('', IndexView.as_view(), name='mydiary_index'),
  path('<int:page>', IndexView.as_view(), name='mydiary_index'),
  path('mydiary_detail/<int:pk>', DetailView.as_view(), name='mydiary_detail'),
  path('mydiary_create', CreateView.as_view(), name='mydiary_create'),
  path('mydiary_edit/<int:pk>', EditView.as_view(), name='mydiary_edit'),
  path('mydiary_delete/<int:pk>', DeleteView.as_view(), name='mydiary_delete'),
  path('mydiary_login', LoginView.as_view(template_name='mydiary/mydiary_login.html'), name='login'),
  path('mydiary_logout', LogoutView.as_view(template_name='mydiary/mydiary_logout.html'), name='logout'),
]