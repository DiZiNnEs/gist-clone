from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import ugettext_lazy as _


class CustomUser(AbstractUser):
    USERNAME_FIELD = 'email'
    email = models.EmailField(_('email address'), unique=True)
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'custom_user'
        verbose_name = 'Custom user'
        verbose_name_plural = 'Custom users'
