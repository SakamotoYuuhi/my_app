# from django.forms import widgets
from django import forms
from .models import MyDiary

class MyDiaryForm(forms.ModelForm):
  class Meta:
    model = MyDiary
    fields = ['topic_title', 'content', 'image']
    widgets = {
      'topic_title': forms.TextInput(attrs={'class':'form-control'}),
      'content': forms.Textarea(attrs={'class':'form-control'}),
      'image': forms.ClearableFileInput(attrs={'class':'form-control-file','multiple': True}),
    }