from rest_framework import serializers
from .models import *


class CategorySer(serializers.ModelSerializer):
    class Meta:
        model = food_category
        fields= ('id', "rus_name")

class SubtypeSer(serializers.ModelSerializer):
    class Meta:
        model = food_subtype
        fields= ('id', "rus_name", 'cat_id')

class ProdSer(serializers.ModelSerializer):
    class Meta:
        model = food_product
        fields= ('id','sub', 'rus_name','calories', 'fat','carbo','protein')