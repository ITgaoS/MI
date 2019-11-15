from django.db import models

# Create your models here.
class User(models.Model):
# Create your models here.
    email=models.EmailField()
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    gender=models.CharField(max_length=10,null=True,blank=True)
    phone=models.CharField(max_length=12,null=True,blank=True)
    age=models.CharField(max_length=10,null=True,blank=True)
    address=models.CharField(max_length=10,null=True,blank=True)
    picture=models.ImageField(upload_to="backstage/images",default="backstage/image/11.jpeg")

