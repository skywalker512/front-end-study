from django.db import models
import django.utils.timezone as timezone


class Article(models.Model):
    title = models.CharField('标题', null=True, blank=True, max_length=50)
    content = models.TextField('正文', null=True, blank=True, max_length=10000)
    tag = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)
    add_date = models.DateTimeField('保存日期', default=timezone.now)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField('标签名', max_length=30)

    def __str__(self):
        return self.name
