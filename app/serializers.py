from .models import Item, Profile
from rest_framework import serializers 

class ItemDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model= Item
		fields= "__all__"

