from django.contrib import admin
from .models import Item, Profile, Order, ItemOrder


admin.site.register(Item)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(ItemOrder)
