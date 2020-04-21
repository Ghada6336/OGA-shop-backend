from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Item ,Profile ,Order  , Basket

class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name',  'picture', 'discription',
                  'price', 'quantity', 'owner', 'gender']

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

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ["username", "first_name", "last_name", "email"]
		read_only_fields = ['username']


class UpdateProfileSerializer(serializers.ModelSerializer):
	user = UserSerializer()

	class Meta:
		model = Profile
		fields = ["user","phone","gender","age","image"]

	def update(self, instance, validated_data):
	
		user_field = validated_data.pop('user', None)
		temp_user_serializer = UserSerializer()
		super().update(instance, validated_data)
		super(UserSerializer, temp_user_serializer).update(instance.user, user_field)
		return instance



class ItemOrderDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = Item
		fields = ['name', 'price']
  
class BasketSerializer(serializers.ModelSerializer):
	item = ItemOrderDetailSerializer()
	class Meta:
		model = Basket
		fields = '__all__'



class OrderSerializer(serializers.ModelSerializer):
	baskets= BasketSerializer(many=True)

	class Meta:
		model = Order
		fields = ["id", "owner",  "baskets"]