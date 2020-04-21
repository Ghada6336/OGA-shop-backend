from django.contrib import admin

# Register your models here.
from .models import Item, Profile ,Order, Basket

admin.site.register(Item)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Basket)
