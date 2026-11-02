from datetime import date

from django.utils import timezone
from rest_framework import serializers

from .models import Reservation

TIME_CHOICES = ["17:30", "18:00", "18:30", "19:00", "19:30", "20:00", "20:30"]
GUEST_CHOICES = [
    "1 Person",
    "2 Personen",
    "3 Personen",
    "4 Personen",
    "5 Personen",
    "6+ Personen",
]


class ReservationSerializer(serializers.ModelSerializer):
    time = serializers.ChoiceField(choices=TIME_CHOICES)
    guests = serializers.ChoiceField(choices=GUEST_CHOICES)
    message = serializers.CharField(
        max_length=1000, required=False, allow_blank=True
    )

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

    def validate_date(self, value: date):
        if value < timezone.localdate():
            raise serializers.ValidationError(
                "Das Datum darf nicht in der Vergangenheit liegen."
            )
        return value
