from django.contrib.auth.models import User

from django.db import models


class Gist(models.Model):
    title = models.CharField(max_length=64, verbose_name='Gist name')
    pub_date = models.DateTimeField(verbose_name='Publication date')
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField()

    class Meta:
        db_table = 'gist'
        verbose_name = 'gist'
        verbose_name_plural = 'gists'
        ordering = ['title']
