from rest_framework import viewsets
from .models import Reservation, Restaurant
from .serializers import ReservationSerializer, RestaurantSerializer


# Create your views here.
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
