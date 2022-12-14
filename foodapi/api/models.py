from django.db import models

# Create your models here.
class food_category(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=255)
    rus_name = models.CharField(max_length=255)

    def __str__(self):
        return self.rus_name

class food_subtype(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=255)
    rus_name = models.CharField(max_length=255)
    cat = models.ForeignKey(food_category, on_delete=models.CASCADE, null=True)
    cat_name = models.CharField(max_length=255)

    def __str__(self):
        return self.rus_name

class food_product(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    cat = models.ForeignKey(food_category, on_delete=models.CASCADE, null=True)
    sub = models.ForeignKey(food_subtype, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    rus_name = models.CharField(max_length=255)
    calories = models.CharField(max_length=255)
    fat = models.CharField(max_length=255)
    carbo = models.CharField(max_length=255)
    protein = models.CharField(max_length=255)
    cat_name = models.CharField(max_length=255)
    sub_name = models.CharField(max_length=255)

    def __str__(self):
        return self.rus_name


class users(models.Model):
    id  = models.IntegerField(null=False, primary_key=True)
    nickname = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, default="Аноним")
    email = models.CharField(max_length=255)
    age = models.IntegerField(default=0)
    weight = models.IntegerField(default=0)
    growth = models.IntegerField(default=0)
    sex = models.IntegerField(default=2)
    base_metabolism = models.IntegerField(default=0)
    def __str__(self):
        return self.id
