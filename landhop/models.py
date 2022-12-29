from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Create your models here.
class User(AbstractUser):
    pass

# Section Model
class Section(models.Model):
    title = models.CharField(max_length=100)
    photo = models.URLField(max_length=500)
    dateCreated = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.title}"

# City Model
class City(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    photo = models.URLField(max_length=500)
    isTop = models.BooleanField(default=False)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, null=True, related_name="section")
    dateCreated = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.title}"

# Sight Model
class Sight(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="user")
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=800)
    photo = models.URLField(max_length=500)
    totalStars = models.FloatField(default=0)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True, related_name="city")
    dateCreated = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.title} by {self.author}"

# Comments
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="userName")
    description = models.CharField(max_length=1000)
    stars = models.FloatField()
    sight = models.ForeignKey(Sight, on_delete=models.CASCADE, null=True, related_name="sight")
    dateCreated = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return f"{self.author}: {self.description} - {self.sight}"