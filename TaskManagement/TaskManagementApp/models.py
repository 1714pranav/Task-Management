from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
# Create your models here.

class CustomUser(AbstractUser):
    username = None

    email = models.EmailField(("email address"),unique=True)

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

CHOICES = ( ('PENDING','Pending'),
           ('IN-PROGRESS','In Progress'),
           ('COMPLETED','Completed'),
)


class Task(models.Model):
    user_id = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=25)  
    description = models.TextField(null=True)
    due_date  = models.DateTimeField(null=True)
    status = models.CharField(max_length=15,choices=CHOICES,default="PENDING") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
