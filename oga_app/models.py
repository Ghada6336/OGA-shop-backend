from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=120)
    discription = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,  related_name="user")

    def __str__(self):
        return self.name
