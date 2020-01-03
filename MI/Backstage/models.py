from django.db import models
# Create your models here.
class CommodityType(models.Model):
    type=models.CharField(max_length=32)
    picture=models.ImageField(upload_to="backstage/images",default="backstage/images/11.jpeg")

class Commodity(models.Model):
    name=models.CharField(max_length=32)
    price=models.FloatField()
    color=models.CharField(max_length=32)
    specification =models.TextField()
    state=models.IntegerField(default=1)
    picture = models.ImageField(upload_to="backstage/images", default="backstage/images/11.jpeg")
    type=models.ForeignKey(to=CommodityType,on_delete=models.CASCADE)
class Goods(models.Model):
    name=models.CharField(max_length=32)
    price=models.CharField(max_length=32)
    color=models.CharField(max_length=32)
    specification =models.TextField()
    state=models.IntegerField(default=1)
    vers=models.CharField(max_length=32)
    picture = models.ImageField(upload_to="backstage/images", default="backstage/images/11.jpeg")
    type=models.ForeignKey(to=CommodityType,on_delete=models.CASCADE)
