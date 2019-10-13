from .serializers import ItemDetailSerializer
from .models import Item
from rest_framework.generics import RetrieveAPIView

class ItemDetail(RetrieveAPIView):
	queryset= Item.objects.all()
	serializer_class= ItemDetailSerializer
	lookup_field="id"
	lookup_url_kwarg="item_id"