from django.db import models


# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()
    message = models.TextField()
    restaurant = models.ForeignKey("Restaurant", on_delete=models.CASCADE, null=True)

    @property
    def google_maps_url(self):
        return f"https://www.google.com/maps/search/?api=1&query={self.restaurant.lat},{self.restaurant.lon}"
    
    @property
    def restaurant_name(self):
        return self.restaurant.name if self.restaurant else None

    def __str__(self):
        return f"{self.name}'s reservation for {self.number_of_people} on {self.date} at {self.time}"


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField()
    description = models.TextField()
    lat = models.FloatField()
    lon = models.FloatField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.name} at {self.address}"
