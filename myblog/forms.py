from django import forms

class MyBlogForm(forms.Form):
  id = forms.IntegerField(label='ID')
  topic_title = forms.CharField(label='タイトル名', \
                widget=forms.TextInput(attrs={'class':'form-control'}))
  content = forms.CharField(label='コンテンツ', \
                widget=forms.Textarea(attrs={'class':'form-control'}))
  image = forms.ImageField(label='写真・画像', required=False, \
                widget=forms.ClearableFileInput(attrs={'multiple': True}))