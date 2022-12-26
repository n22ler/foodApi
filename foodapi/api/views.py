from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import *

from .models import *


class CatApiView(generics.ListCreateAPIView): #выдаем все категории
    queryset = food_category.objects.all()
    serializer_class = CategorySer
    permission_classes= (IsAuthenticated,)

class SubApiView(generics.ListCreateAPIView): #выдаем все подкатегории
    queryset = food_subtype.objects.all()
    serializer_class = SubtypeSer
    permission_classes= (IsAuthenticated,)


class ProdApiView(generics.ListCreateAPIView): #выдаем все продукты
    queryset = food_product.objects.all()
    serializer_class = ProdSer
    permission_classes= (IsAuthenticated,)

class UserApiView(generics.ListCreateAPIView): # выдаем пользователя
    queryset = users.objects.all()
    serializer_class= UserSer
    def get_queryset(self):
        return users.objects.filter(id = self.kwargs['id'])

class UpdateUserData(generics.UpdateAPIView): # обновляем данные в акк пользователя
    queryset = users.objects.all()
    serializer_class = UpdateUserDataSer