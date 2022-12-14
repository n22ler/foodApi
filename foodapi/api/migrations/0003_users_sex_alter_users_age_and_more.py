# Generated by Django 4.1 on 2022-11-30 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='sex',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='users',
            name='base_metabolism',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='users',
            name='growth',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='users',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]
