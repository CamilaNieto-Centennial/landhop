from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    pass

# Auction Listings Model
class Section(models.Model):
    title = models.CharField(max_length=100)
    photo = models.URLField(max_length=500)
    dateCreated = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.title}"