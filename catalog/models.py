from django.contrib.auth.models import AbstractUser
from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Redactor(AbstractUser):
    years_of_expirience = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "redactor"
        verbose_name_plural = "redactors"
        ordering = ["username"]

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    topic = models.ForeignKey("Topic", on_delete=models.CASCADE)
    publishers = models.ManyToManyField("Redactor", related_name="newspapers")

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        date = self.published_date.strftime("%d/%m/%Y")

        return f"{self.title} (topic: {self.topic}, date: {date})"
