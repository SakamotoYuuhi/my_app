from django.urls import path
from .views import ContactFormView, ContactResultView

urlpatterns = [
  path('', ContactFormView.as_view(), name='index'),
  path('contact_result', ContactResultView.as_view(), name='contact_result'),
]