from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from .models import FlightTimings
from rest_framework.views import APIView
from .serializers import FlightTimingSerializers

class FlightTimingView(APIView):
    def post(self,request,format=None):
        route = request.data.get('id')
        print(route)

        if route is not None:
            try:
                flightdata = FlightTimings.objects.get(id=route)
                # print(flightdata)
                serializer =FlightTimingSerializers(flightdata)
                # print(serializer.data)
                return Response(serializer.data, status=status.HTTP_200_OK)
               
            except FlightTimings.DoesNotExist:
                return Response({"message": "Flight Details not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "Flight route not found"}, status=status.HTTP_404_NOT_FOUND)
