from rest_framework import serializers
from .models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            "id",
            "name",
            "email",
            "date",
            "time",
            "guests",
            "message",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]