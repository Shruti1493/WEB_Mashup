from rest_framework import serializers
from .models import FlightTimings

class FlightTimingSerializers(serializers.ModelSerializer):
    class Meta:
        model = FlightTimings
        fields = '__all__'
