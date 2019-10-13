from django.shortcuts import render

from rest_framework.generics import (ListAPIView)

from .models import Item
from .serializers import (ItemSerializer)

# Create your views here.
class ItemsList(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer