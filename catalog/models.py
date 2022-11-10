from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Redactor(AbstractUser):
    years_of_expirience = models.IntegerField()

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"
        ordering = ["username"]
