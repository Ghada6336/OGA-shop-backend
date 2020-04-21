
from rest_framework.generics import ListAPIView, CreateAPIView , RetrieveUpdateAPIView

from oga_app.models import Item,Profile , Order ,Basket
from .serializers import ItemListSerializer, UserCreateSerializer ,UpdateProfileSerializer, OrderSerializer

from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.views import APIView
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST)
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter


class SockListView(ListAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemListSerializer

class ProfileUpdateView(RetrieveUpdateAPIView):
    serializer_class = UpdateProfileSerializer

    def get_object(self):
        return Profile.objects.get(user=self.request.user)

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer




class OrderItems(APIView):
	serializer_class = OrderSerializer

	def post(self, request):

		order  = Order.objects.create( owner = request.user)
		items = request.data['baskets']
		for item in items:
			Basket.objects.create(
				item_id=item['id'],
				quantity= item['quantity'],
				order=order
			)
		return Response(self.serializer_class(order).data, status=HTTP_200_OK)


