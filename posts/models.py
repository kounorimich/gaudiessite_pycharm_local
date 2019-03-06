from django.db import models
from markdownx.models import MarkdownxField
# Create your models here.


class Post(models.Model):
    """投稿モデル"""
    class Meta:
        db_table = 'post'

    title = models.CharField(verbose_name='タイトル', max_length=100)
    published = models.DateField(verbose_name='投稿日', blank=True)
    image = models.ImageField(verbose_name='画像', blank=True)
    body = MarkdownxField(verbose_name='本文')


    def __str__(self):
        return self.title

    def summary(self):
        return self.body.split('。')[0]
