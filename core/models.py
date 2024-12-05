from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Amigo(AbstractUser):
    bio = models.TextField()

class Item(models.Model):
    nome = models.CharField(max_length=50)
    link = models.CharField(max_length=150, null=True, blank=True)

class Escolha(models.Model):
    momento = models.DateTimeField(auto_now=False, auto_now_add=True)
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    compromissado = models.ForeignKey(Amigo, on_delete=models.CASCADE)
