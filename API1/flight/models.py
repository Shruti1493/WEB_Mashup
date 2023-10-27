from django.db import models
import datetime
class FlightRoute(models.Model):
    route_name = models.CharField(max_length=100, unique=True, help_text="Route name, e.g., Mumbai-Delhi")
    departure_city = models.CharField(max_length=50, help_text="Departure city")
    arrival_city = models.CharField(max_length=50, help_text="Arrival city")
    distance = models.PositiveIntegerField(help_text="Distance in kilometers")
    duration = models.DurationField(help_text="Flight duration")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in USD")
    departure_time = models.TimeField(
        help_text="Departure time",
        blank=True,
        default=datetime.time(8, 0)  # Default departure time is 08:00:00
    )

    arrival_time = models.TimeField(
        help_text="Arrival time",
        blank=True,
        default=datetime.time(16, 0)  # Default arrival time is 16:00:00
    )
    def __str__(self):
        return f" Flight id is: {self.id} , Flight route is {self.route_name}"

    class Meta:
        verbose_name = "Flight Route"
        verbose_name_plural = "Flight Routes"
