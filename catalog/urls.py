from django.urls import path
from rest_framework.routers import DefaultRouter

from catalog.FleetLogsViews import fleet_logs_detail, fleet_logs_list_create
from catalog.RentalEventsViews import rental_events_detail, rental_events_list_create
from .views import VehiclesViewSet, RentalsViewSet

router = DefaultRouter()
router.register(r"vehicles", VehiclesViewSet, basename="vehicles")
router.register(r"rentals", RentalsViewSet, basename="rentals")

urlpatterns = [
    
 
    path("fleet-logs/", fleet_logs_list_create),
    path("fleet-logs/<str:id>/", fleet_logs_detail),
    path("rental-events/", rental_events_list_create),
    path("rental-events/<str:id>/", rental_events_detail),
]
urlpatterns += router.urls









