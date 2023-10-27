from rest_framework import serializers
from .models import FlightRoute

class FlightSerializers(serializers.ModelSerializer):
    class Meta:
        model = FlightRoute
        fields = '__all__'
