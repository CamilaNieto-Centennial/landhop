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

class City(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    photo = models.URLField(max_length=500)
    isTop = models.BooleanField(default=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, related_name="section")
    dateCreated = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.title}"