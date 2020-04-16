
from rest_framework.generics import ListAPIView, CreateAPIView , RetrieveUpdateAPIView

from oga_app.models import Item,Profile
from .serializers import ItemListSerializer, UserCreateSerializer  ,UpdateProfileSerializer

from rest_framework_simplejwt.views import TokenObtainPairView

class SockListView(ListAPIView):

    queryset = Item.objects.all()
    serializer_class = ItemListSerializer

class ProfileUpdateView(RetrieveUpdateAPIView):
	serializer_class = UpdateProfileSerializer

	def get_object(self):
		return Profile.objects.get(user=self.request.user)

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer

