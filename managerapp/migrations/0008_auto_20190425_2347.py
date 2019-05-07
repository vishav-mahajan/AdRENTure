# Generated by Django 2.0.6 on 2019-04-25 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managerapp', '0007_auto_20190425_2308'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclesdetails',
            name='abs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vehiclesdetails',
            name='airbags',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vehiclesdetails',
            name='seats',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='vehiclesdetails',
            name='transmission',
            field=models.CharField(default='', max_length=20),
        ),
    ]