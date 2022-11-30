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

class UserSer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ('id','first_name', 'age','weight', 'growth','base_metabolism', 'sex','email')


class UpdateUserDataSer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = ('first_name', 'age','weight', 'growth','base_metabolism', 'sex')

    def update(self, instance, validated_data):
        (value_fn, )= validated_data['first_name'],
        (value_a ,)= validated_data['age'],
        (value_g ,)= validated_data['growth'],
        (value_w ,)= validated_data['weight'],
        (value_bm,) = validated_data['base_metabolism'],
        value_s= validated_data['sex']
        instance.first_name =value_fn 
        instance.age =value_a
        instance.growth =value_g
        instance.weight =value_w
        instance.base_metabolism =value_bm
        instance.sex =value_s
        instance.save()
        return instance