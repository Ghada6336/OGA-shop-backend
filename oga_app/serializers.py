from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Item


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name',  'picture', 'price', 'quantity']


# Your model is very simple.
# It doesn't need a
# Just make the ItemListSerializer return all the fields you want
class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['discription', 'id', 'picture', 'quantity', 'size', 'gender']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        password = serializers.CharField(write_only=True)
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        new_user = User(username=username)
        new_user.set_password(password)
        new_user.save()
        return validated_data
