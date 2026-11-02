from datetime import timedelta

from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase

from .models import Reservation


class ReservationApiTests(APITestCase):
    def setUp(self):
        self.url = reverse("reservation-create")
        self.payload = {
            "name": "Max Mustermann",
            "email": "max@beispiel.de",
            "date": (timezone.localdate() + timedelta(days=1)).isoformat(),
            "time": "19:00",
            "guests": "2 Personen",
            "message": "",
        }

    def test_creates_reservation(self):
        response = self.client.post(self.url, self.payload, format="json")
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Reservation.objects.count(), 1)

    def test_rejects_past_date(self):
        self.payload["date"] = (timezone.localdate() - timedelta(days=1)).isoformat()
        response = self.client.post(self.url, self.payload, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("date", response.data)

    def test_rejects_invalid_time_and_guests(self):
        self.payload["time"] = "03:00"
        self.payload["guests"] = "100"
        response = self.client.post(self.url, self.payload, format="json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("time", response.data)
        self.assertIn("guests", response.data)
