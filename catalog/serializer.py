from rest_framework import serializers
from .models import Vehicles, Rentals

class VehiclesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicles
        fields = ["id", "plate", "brand","daily_rate", "is_available"]

class RentalsSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.CharField(source="vehicle.plate", read_only=True)

    class Meta:
        model = Rentals
        fields = ["id", "vehicle", "vehicle_plate", "customer_name", "total", "status", "created_at"]

