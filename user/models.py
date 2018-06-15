from django.db import models

# Create your models here.


class User(models.Model):
    userName = models.CharField(max_length=30,db_column='user_name')
    passWord = models.CharField(max_length=36,db_column='pass_word')
    email = models.EmailField()
    gender = models.CharField(max_length=4)
    registerTime = models.DateTimeField(auto_now_add=True)
    updateTime = models.DateTimeField(auto_now=True)