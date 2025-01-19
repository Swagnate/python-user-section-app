# sections/models.py

from django.db import models
from django.contrib.auth.models import User

class Section(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='sections', blank=True)

    def __str__(self):
        return self.name