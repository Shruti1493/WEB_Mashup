# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework import status
# from .models import FlightRoute
# from rest_framework.views import APIView
# from .serializers import FlightSerializers
# # Create your views here.
# class FlightRouteView(APIView):
#     def post(self,request,format = None):
#         route = request.data.get('route')

#         if route is not None:
#             try:
#                 flightdata = FlightRoute.objects.get(route_name = route)
#                 serializer = FlightSerializers(flightdata)
#                 # if serializer.is_valid():
#                 return Response(serializer.data,status=status.HTTP_200_OK)
#             except FlightRoute.DoesNotExist:
#                 return Response({"message":"Flight Details not found"},status = status.HTTP_404_NOT_FOUND)
#         else:
#             return Response({"message":"Flight route not found"},status = status.HTTP_404_NOT_FOUND)



from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import FlightRoute
from rest_framework.views import APIView
from .serializers import FlightSerializers
class FlightRouteView(APIView):
    def post(self, request, format=None):
        route = request.data.get('route')
        print(route)

        if route is not None:
            try:
                flightdata = FlightRoute.objects.get(route_name=route)
                # print(flightdata)
                serializer = FlightSerializers(flightdata)
                # print(serializer.data)
                return Response(serializer.data, status=status.HTTP_200_OK)
               
            except FlightRoute.DoesNotExist:
                return Response({"message": "Flight Details not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "Flight route not found"}, status=status.HTTP_404_NOT_FOUND)
