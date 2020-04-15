
from rest_framework.generics import ListAPIView, CreateAPIView

from oga_app.models import Item
from .serializers import ItemListSerializer, UserCreateSerializer , MyTokenObtainPairSerializer

from rest_framework_simplejwt.views import TokenObtainPairView

class SockListView(ListAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemListSerializer


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer