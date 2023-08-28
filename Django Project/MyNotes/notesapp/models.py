from django.db import models
from datetime import datetime

# Create your models here.

class userSignup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()


class mynotes(models.Model):
    #created=models.DateTimeField(auto_now_add=True)
    created=models.DateTimeField(default=datetime.now(),blank=True)
    query=models.CharField(max_length=100)
    opt=models.CharField(max_length=100)
    myfiles=models.FileField(upload_to='Files')
    comments=models.TextField()


class callback(models.Model):
    created=models.DateTimeField(default=datetime.now(),blank=True)
    fullname=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    email=models.EmailField()
    msg=models.TextField()
