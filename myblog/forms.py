from django import forms

class MyBlogForm(forms.Form):
  id = forms.IntegerField(label='ID')
  topic_title = forms.CharField(label='タイトル名', \
                widget=forms.TextInput(attrs={'class':'form-control'}))
  content = forms.CharField(label='コンテンツ', \
                widget=forms.TextInput(attrs={'class':'form-control'}))