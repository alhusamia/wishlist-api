from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .permissions import IsAuthor
from items.models import Item,FavoriteItem
from .serializers import RegisterSerializer,ItemSerializer,ItemDetailSerializer


# Create your views here.
class ItemListView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']

class ItemDetailView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'itemapi_id'
    permission_classes = [IsAuthor]



class Register(CreateAPIView):
    serializer_class = RegisterSerializer
