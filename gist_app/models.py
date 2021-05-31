from django.contrib.auth.models import User

from django.db import models

from django.urls import reverse

from gist_clone import settings


class Gist(models.Model):
    title = models.CharField(max_length=64, verbose_name='Gist name')
    pub_date = models.DateTimeField(verbose_name='Publication date')
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse('detail-gist', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'gist'
        verbose_name = 'gist'
        verbose_name_plural = 'gists'
        ordering = ['title']
