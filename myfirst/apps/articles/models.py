from django.db import models
import datetime
from django.utils import timezone


class Article(models.Model):
    article_title = models.CharField('Name of article', max_length=200)
    article_text = models.TextField('Text of article')
    pub_date = models.DateTimeField('Date of public')

    class Meta:
        verbose_name = "Capable Article"
        verbose_name_plural = "Capable Articles"

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author_name = models.CharField("Authors name", max_length=50)
    comment_text = models.CharField("Comments text", max_length=200)

    class Meta:
        verbose_name = "Capable Comment"
        verbose_name_plural = "Capable Comments"

    def __str__(self):
        return self.author_name
