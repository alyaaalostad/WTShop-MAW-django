from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView)

from .models import Item, Profile
from .serializers import (ItemSerializer, RegisterSerializer, ProfileSerializer)


class ItemsList(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class Register(CreateAPIView):
    serializer_class = RegisterSerializer


class UserProfile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(user=self.request.user)
        serializer_class = ProfileSerializer(profile)
        return Response(serializer_class.data, status = status.HTTP_200_OK)

    def put(self, request):
        profile = Profile.objects.get(user=self.request.user)
        serializer_class = ProfileSerializer(profile, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status = status.HTTP_200_OK)
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

