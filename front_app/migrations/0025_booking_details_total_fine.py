# Generated by Django 2.0.6 on 2019-05-04 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_app', '0024_auto_20190504_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_details',
            name='total_fine',
            field=models.BigIntegerField(default=0),
        ),
    ]