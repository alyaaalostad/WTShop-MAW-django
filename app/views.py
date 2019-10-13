from django.shortcuts import render

from rest_framework.generics import (ListAPIView, RetrieveAPIView)

from .models import Item
from .serializers import (ItemSerializer, ItemDetailSerializer)

# Create your views here.
class ItemsList(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer

class ItemDetail(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "item_id"