# Generated by Django 2.0.6 on 2019-04-05 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managerapp', '0002_auto_20190406_0029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclesdetails',
            name='vehicle_isavailable',
            field=models.BooleanField(default=True),
        ),
    ]