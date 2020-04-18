from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save, pre_delete, pre_save
from django.dispatch import receiver


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


class Profile(models.Model):
    GENDER = (
        ("F", "Female"),
        ("M", "Male")
    )
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    phone = models.PositiveIntegerField(null=True)
    gender = models.CharField(choices=GENDER, max_length=2, null=True)
    age = models.PositiveIntegerField(null=True)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# check


class Order(models.Model):
    user_order = models.ForeignKey(
        User, on_delete=models.CASCADE,  related_name="user_order")
    is_order = models.BooleanField(null=True)

    def __str__(self):
        return self.user_order.username


class OrderItem(models.Model):
    order_owner = models.ForeignKey(
        "Order", on_delete=models.CASCADE,  related_name="order_owner")
    order_item = models.ForeignKey(
        Item, on_delete=models.CASCADE,  related_name="order_item")
    quantity_num = models.PositiveIntegerField(null=True)
