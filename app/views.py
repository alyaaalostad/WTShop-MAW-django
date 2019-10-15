from django.shortcuts import render

from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView)

from .models import Item
from .serializers import (ItemSerializer, RegisterSerializer)


class ItemsList(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer


class ItemDetail(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    lookup_field = "id"
    lookup_url_kwarg = "item_id"


class Register(CreateAPIView):
    serializer_class = RegisterSerializer
