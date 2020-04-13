
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from oga_app.models import Item
from .serializers import ItemListSerializer, UserCreateSerializer, DetailSerializer


class ListView(ListAPIView):
    # Don't just name this ListView
    # What is it a list of?
    # E.g. PotatoListView or SockListView
    queryset = Item.objects.all()
    serializer_class = ItemListSerializer


class DetailView(RetrieveAPIView):
    # Your model is very simple.
    # You don't need a detail view.
    # Just return the full object in the list view.
    queryset = Item.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
