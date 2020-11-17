from django.db import models

class MyBlogModel(models.Model):
  topic_title = models.CharField(max_length=50)
  content = models.CharField(max_length=200)

  def __str__(self):
    return '<Friend:id=' + str(self.id) + ', タイトル名:' + \
            self.topic_title + '>'