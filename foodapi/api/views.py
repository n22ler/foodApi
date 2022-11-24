from django.shortcuts import render

from rest_framework import generics
from .serializers import *
from .models import *


class CatApiView(generics.ListCreateAPIView):
    queryset = food_category.objects.all()
    serializer_class = CategorySer

class SubApiView(generics.ListCreateAPIView):
    queryset = food_subtype.objects.all()
    serializer_class = SubtypeSer


class ProdApiView(generics.ListCreateAPIView):
    queryset = food_product.objects.all()
    serializer_class = ProdSer