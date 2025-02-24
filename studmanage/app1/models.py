from django.db import models

# Create your models here.

class register(models.Model):
    name=models.CharField(max_length=30)
    gender=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.BigIntegerField()
    img=models.FileField(upload_to='photo')

class log(models.Model):
    uname=models.CharField(max_length=40)
    upwd=models.CharField(max_length=20)
    utype=models.CharField(max_length=50)
    uid=models.ForeignKey(register,on_delete=models.CASCADE)

