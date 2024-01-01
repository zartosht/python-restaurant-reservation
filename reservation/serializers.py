from rest_framework import serializers
from .models import Reservation, Restaurant


class ReservationSerializer(serializers.ModelSerializer):
    restaurant = serializers.PrimaryKeyRelatedField(queryset=Restaurant.objects.all())

    class Meta:
        model = Reservation
        fields = [
            "id",
            "name",
            "email",
            "phone",
            "date",
            "time",
            "number_of_people",
            "message",
            "restaurant",
            "restaurant_name",
        ]

    def create(self, validated_data):
        restaurant = validated_data.get("restaurant")
        number_of_people = validated_data.get("number_of_people")
        reservation_date = validated_data.get("date")
        reservation_time = validated_data.get("time")

        if not self.is_capacity_available(
            restaurant, number_of_people, reservation_date, reservation_time
        ):
            raise serializers.ValidationError(
                "Restaurant does not have enough capacity for the requested number of people."
            )
        return Reservation.objects.create(**validated_data)
    
    def is_capacity_available(self, restaurant, number_of_people, reservation_date, reservation_time):
        reservations = Reservation.objects.filter(
            restaurant=restaurant, date=reservation_date, time=reservation_time
        )
        reserved_capacity = sum([r.number_of_people for r in reservations])
        return restaurant.capacity >= reserved_capacity + number_of_people


class RestaurantSerializer(serializers.ModelSerializer):
    google_maps_url = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = [
            "id",
            "name",
            "address",
            "phone",
            "email",
            "website",
            "description",
            "lat",
            "lon",
            "google_maps_url",
            "capacity",
        ]

    def get_google_maps_url(self, obj):
        return f"https://www.google.com/maps/search/?api=1&query={obj.lat},{obj.lon}"
