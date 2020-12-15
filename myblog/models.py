from django.db import models

class MyBlog(models.Model):
  id = models.IntegerField(primary_key=True, unique=True)
  topic_title = models.CharField(max_length=50)
  content = models.CharField(max_length=200)
  image = models.ImageField(upload_to='', null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    db_table = 'myblog'

  def __str__(self):
    return 'タイトル名:' + self.topic_title