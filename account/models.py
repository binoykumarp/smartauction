from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.





class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    image=models.ImageField(upload_to="P_image")
    price=models.IntegerField()
    date=models.DateField(auto_now_add=True,null=True)
    Au_Date=models.DateField(null=True)
    options=(
        ('vehicle','vehicle'),
        ('plote','plote'),
        ('house','house'),
        ('building','building'),
        ('land','land'),
        ('others','others'),
    )
    category=models.CharField(max_length=100,choices=options,null=True)

class Aucart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,default='aucart')
    money=models.IntegerField(null=True)



class Auctions(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    phone=models.IntegerField()
    address=models.CharField(max_length=500)


class Room(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=500)
    slug=models.SlugField(unique=True)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('date_added',)