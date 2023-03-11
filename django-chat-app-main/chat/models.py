from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_message = models.BooleanField(default=False)
    bot_message = models.BooleanField(default=False)
    value = models.CharField(max_length=1000000)
    date = models.CharField(max_length=1000000,null=True,blank=True)
    time = models.CharField(max_length=1000000,null=True,blank=True)