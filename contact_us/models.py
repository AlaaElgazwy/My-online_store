from django.db import models

# Create your models here.
class Contact_us(models.Model):

    name=models.CharField(max_length=200)
    email=models.EmailField()
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)