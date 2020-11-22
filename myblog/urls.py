from django.urls import path
from .views import IndexView, CreateView, DetailView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', IndexView.as_view(), name='index'),
  path('<int:page>', IndexView.as_view(), name='index'),
  path('create', CreateView.as_view(), name='create'),
  path('detail/<int:pk>', DetailView.as_view(), name='detail'),
]

# 画像アップロード用にsettings.pyにパスを通すために追記
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)