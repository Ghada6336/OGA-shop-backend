from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=120)
    discription = models.TextField(max_length=350)
    picture = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,  related_name="user")
    
    CHOICES = (
        ('L', 'large'),
        ('XL', 'x-large'),
        ('S', 'small'),
        ('M', 'medium'),
    )
    size = models.CharField(max_length=2, choices=CHOICES)

    def __str__(self):
        return self.name
