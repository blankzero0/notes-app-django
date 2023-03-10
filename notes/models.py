from django.db import models
from django.urls import reverse

# Create your models here.
class Note(models.Model):
    summary = models.CharField(max_length=255)
    details = models.CharField(max_length=1000)
    done = models.BooleanField()

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})
