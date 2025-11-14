from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):

    name=models.CharField(max_length=200)



    def __str__(self):
        return self.name       


class Product(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    description=models.TextField()
    price=models.DecimalField(max_digits=8,decimal_places=2)
    image=models.ImageField(upload_to='images',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



 

