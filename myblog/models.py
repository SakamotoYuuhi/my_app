from django.db import models

class MyBlog(models.Model):
  title = models.CharField(max_length=100)
  url = models.SlugField()
  text = models.TextField()
  category = models.CharField(max_length=20)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'myblog'

  def __str__(self):
    return 'タイトル名:' + self.title