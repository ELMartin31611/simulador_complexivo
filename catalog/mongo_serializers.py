
from rest_framework import serializers


class Estado:
    CREATED = "creado"
    UPDATED = "actualizado"
    MAINTENANCE = "mantenimiento"
    DISABLED = "deshabilitado"

    CHOICES = [
        (CREATED, "Creado"),
        (UPDATED, "Actualizado"),
        (MAINTENANCE, "Mantenimiento"),
        (DISABLED, "Deshabilitado"),
    ]


class Estadosx:
    WEB = "WEB"
    MOBILE = "MOBILE"
    SYSTEM = "SYSTEM"

    CHOICES = [
        (WEB, "web"),
        (MOBILE, "mobile"),
        (SYSTEM, "system"),
    ]


class FleetLogsSerializer(serializers.Serializer):
    vehicle_id = serializers.IntegerField()
    note = serializers.CharField(max_length=120)
    action = serializers.ChoiceField(
        choices=Estado.CHOICES,
        default=Estado.CREATED
    )
    source = serializers.ChoiceField(
        choices=Estadosx.CHOICES,
        default=Estadosx.WEB
    )
    created_at = serializers.DateTimeField(required=False)


class Estados:
    CREATED = "creado"
    PICKED_UP = "recogido"
    RETURNED = "devuelto"
    PAID = "pagado"
    CANCELLED = "cancelado"

    CHOICES = [
        (CREATED, "Creado"),
        (PICKED_UP, "Recogido"),
        (RETURNED, "Devuelto"),
        (PAID, "Pagado"),
        (CANCELLED, "Cancelado"),
    ]


class RentalEventsSerializer(serializers.Serializer):
    rentals_id = serializers.IntegerField()
    note = serializers.CharField(max_length=120)
    event_type = serializers.ChoiceField(
        choices=Estados.CHOICES,
        default=Estados.CREATED
    )
    source = serializers.ChoiceField(
        choices=Estadosx.CHOICES,
        default=Estadosx.WEB
    )
    created_at = serializers.DateTimeField(required=False)     

