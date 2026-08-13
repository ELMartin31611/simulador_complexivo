from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Vehicles, Rentals
from .serializers import VehiclesSerializer, RentalsSerializer
from .permissions import IsAdminOrReadOnly

class VehiclesViewSet(viewsets.ModelViewSet):
    queryset = Vehicles.objects.all().order_by("id")
    serializer_class = VehiclesSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["plate", "brand", "daily_rate"]
    ordering_fields = ["id", "plate", "brand", "daily_rate", "is_available"]

class RentalsViewSet(viewsets.ModelViewSet):
    queryset = Rentals.objects.select_related("vehicle").all().order_by("-id")
    serializer_class = RentalsSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["vehicle"]
    search_fields = ["customer_name", "total", "status", "vehicle__plate"]
    ordering_fields = ["id", "customer_name", "total", "status", "vehicle__plate", "created_at"]

