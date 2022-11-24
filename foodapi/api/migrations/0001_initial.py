# Generated by Django 4.1 on 2022-11-24 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='food_category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('rus_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='food_subtype',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('rus_name', models.CharField(max_length=255)),
                ('cat_name', models.CharField(max_length=255)),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.food_category')),
            ],
        ),
        migrations.CreateModel(
            name='food_product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('rus_name', models.CharField(max_length=255)),
                ('calories', models.CharField(max_length=255)),
                ('fat', models.CharField(max_length=255)),
                ('carbo', models.CharField(max_length=255)),
                ('protein', models.CharField(max_length=255)),
                ('cat_name', models.CharField(max_length=255)),
                ('sub_name', models.CharField(max_length=255)),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.food_category')),
                ('sub', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.food_subtype')),
            ],
        ),
    ]