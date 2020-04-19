from django.db import models
from django.contrib.auth.models import User
# Create your models here.
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()
    shopname = models.CharField(max_length=120)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


class Order(models.Model):
    user_order = models.ForeignKey(
        User, on_delete=models.CASCADE,  related_name="user_order")
    is_order = models.BooleanField(null=True)

    def str(self):
        return self.user_order.username


class OrderItem(models.Model):
    order_owner = models.ForeignKey(
        "Order", on_delete=models.CASCADE,  related_name="order_owner")
    order_item = models.ForeignKey(
        Item, on_delete=models.CASCADE,  related_name="order_item")
    quantity_num = models.PositiveIntegerField(null=True)
