# from django import forms
# from .models import MyBlog

# class MyBlogForm(forms.ModelForm):
#   class Meta:
#     model = MyBlog
#     fields = ['title', 'content', 'image']
#     widgets = {
#       'topic_title': forms.TextInput(attrs={'class':'form-control'}),
#       'content': forms.Textarea(attrs={'class':'form-control'}),
#       'image': forms.ClearableFileInput(attrs={'class':'form-control-file','multiple': True}),
#     }