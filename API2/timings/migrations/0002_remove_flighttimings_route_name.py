# Generated by Django 4.2.6 on 2023-10-27 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flighttimings',
            name='route_name',
        ),
    ]
