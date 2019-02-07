from django.db import models

# Create your models here.
class Live(models.Model):
    date = models.DateField(verbose_name='日程')
    image = models.ImageField(verbose_name='画像(任意）', upload_to='lives', blank=True)
    venue = models.CharField(verbose_name='会場', max_length=100)
    venue_url = models.URLField(verbose_name='会場URL（任意）', blank=True)
    title = models.CharField(verbose_name='イベント名（任意）', max_length=100, blank=True)
    detail = models.TextField(verbose_name='詳細（任意）', blank=True)

    def __str__(self):
        return self.date.strftime('%Y/%m/%d') + '' + self.venue


