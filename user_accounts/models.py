from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_account(models.Model):
    user = models.OneToOneField(User, related_name="account_tracker" , on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    age = models.IntegerField(default=0)

    
