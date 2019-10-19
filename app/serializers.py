from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from django.contrib.auth.models import User

from .models import Item, Profile, Order, ItemOrder


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ["username", "password"]
       
    def create(self, validated_data):
        new_user = User(**validated_data)
        new_user.set_password(validated_data["password"])
        new_user.save()
        return validated_data


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]



class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ["user", "number", "bio", "image"]

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer()
        super().update(instance, validated_data)
        super(UserSerializer, user_serializer).update(instance.user,user_data)
        return instance

class ItemOrderSerializer(serializers.ModelSerializer):
    item = ItemSerializer();

    class Meta: 
        model = ItemOrder
        fields = ["item", "quantity"]

class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer();
    midorders = ItemOrderSerializer(many=True);

    class Meta:
        model = Order
        fields = ["user", "midorders"]





