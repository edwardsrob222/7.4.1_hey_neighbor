from django.db import models
from django.urls import reverse


class Tools(models.Model):

    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name

    def get_absolut_url(self):
        return reverse('tools:index')
