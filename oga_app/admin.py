from django.contrib import admin

# Register your models here.
from .models import Item, Profile

admin.site.register(Item)
admin.site.register(Profile)
