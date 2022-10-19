from tkinter import CASCADE
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
