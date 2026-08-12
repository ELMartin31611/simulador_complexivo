from django.db import models

class Vehicles(models.Model):
    plate = models.CharField(max_length=10, unique=True)
    brand = models.CharField(max_length=40, unique=True)
    daily_rate = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.plate

  

class Estado(models.TextChoices):
        RESERVED = "reservado", "Reservado"
        ACTIVE = "activo", "Activo"
        CLOSED = "cerrado", "Cerrado"
        CANCELLED = "cancelado", "Cancelado"


class Rentals(models.Model):
    vehicle_id = models.ForeignKey(Vehicles, on_delete=models.PROTECT, related_name="vehiculos")
    customer_name = models.CharField(max_length=120)
    total = models.DecimalField(
        max_digits=10, 
        decimal_places=2,  
        default=0
    )
    status = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.ACTIVE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Vehicles.brand} {self.customer_name}"
