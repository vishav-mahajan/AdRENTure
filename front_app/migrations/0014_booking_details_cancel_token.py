# Generated by Django 2.0.6 on 2019-05-02 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_app', '0013_booking_details_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_details',
            name='cancel_token',
            field=models.CharField(default='', max_length=255),
        ),
    ]