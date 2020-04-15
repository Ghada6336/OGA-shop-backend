from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Item


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name',  'picture', 'discription',
                  'price', 'quantity', 'owner', 'gender']


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        password = serializers.CharField(write_only=True)
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        new_user = User(username=username,
                        first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return validated_data
