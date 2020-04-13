from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    SIZES = (
        ('L', 'large'),
        ('XL', 'x-large'),
        ('S', 'small'),
        ('M', 'medium'),
    )

    GENDERS = (
        ('M', 'male'),
        ('F', 'female'),
    )

    name = models.CharField(max_length=120)
    discription = models.TextField()
    picture = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    size = models.CharField(max_length=2, choices=SIZES)
    gender = models.CharField(max_length=1, choices=GENDERS)

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE,  related_name="user")

    def __str__(self):
        return self.name
