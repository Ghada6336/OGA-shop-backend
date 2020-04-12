
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from oga_app.models import Item
from .serializers import ItemListSerializer, UserCreateSerializer, DetailSerializer


class ListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer


class DetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
