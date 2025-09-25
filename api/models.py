from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class Transaction(models.Model): 
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  text = models.CharField(max_length=255)
  amount = models.DecimalField(max_digits=10, decimal_places=2)
  created_at = models.DateTimeField(auto_now_add=True)


  class Meta: 
    ordering = ['created_at']

  
  def __str__(self):
    return f"{self.text}" ({self.amount})


# Modèle pour les utilisateurs
class User(AbstractUser):
  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
  age = models.IntegerField()
  profession = models.CharField(max_length=255)

  class Meta: 
    ordering = ['-date_joined']

  def __str__(self):
    return self.username