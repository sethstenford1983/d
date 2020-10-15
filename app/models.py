from django.db import models

# Create your models here.
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255) # заголовок поста
    datetime = models.DateTimeField(u'Дата публикации') # дата публикации
    content = models.TextField(max_length=10000) # текст поста
    author = models.CharField(max_length=255,default= '50') # имя автора
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id
from django.db import models
from  django.contrib.auth.models import User

class Client(models.Model):
    address = models.CharField('Address', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)