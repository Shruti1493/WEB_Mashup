from django.db import models

# Create your models here.

class FlightTimings(models.Model):
    # route_name = models.CharField(max_length=100, unique=True, help_text="Route name, e.g., Mumbai-Delhi")
    BusinessClassprice = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in USD")
    PremiumEconomy = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in USD")
    EconomyClass = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in USD")
    departure_time = models.TimeField(help_text="Departure time")
    arrival_time = models.TimeField(help_text="Arrival time")

    def __str__(self):
        return f" Flight id is: {self.id}"

   
