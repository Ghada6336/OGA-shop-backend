from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Item

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name',  'picture', 'discription',
                  'price', 'quantity', 'owner', 'gender']



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username,
        token['email'] = user.email,

        # ...
        return token

    
class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        password = serializers.CharField(write_only=True)
        model = User
        fields = ['username', 'password','first_name','last_name','email']

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        first_name = validated_data['first_name']
        last_name = validated_data['last_name']
        email = validated_data['email']
        new_user = User(username=username, first_name=first_name, last_name=last_name,email=email)
        new_user.set_password(password)
        new_user.save()
        return validated_data
