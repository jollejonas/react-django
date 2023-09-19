from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # Remove username
    username: None
    
    # Add unique to email field
    email = models.CharField(max_length=150, unique=True)
    
    # Set email as username
    USERNAME_FIELD = "email" 
    REQUIRED_FIELDS = []