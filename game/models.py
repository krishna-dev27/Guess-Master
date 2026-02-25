from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Score(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    score=models.IntegerField(default=0)    