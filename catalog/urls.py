from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import VehiclesViewSet, RentalsViewSet

router = DefaultRouter()
router.register(r"vehicles", VehiclesViewSet, basename="vehicles")
router.register(r"rentals", RentalsViewSet, basename="rentals")

urlpatterns = []
urlpatterns += router.urls









