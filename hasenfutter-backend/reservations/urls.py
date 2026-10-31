from django.urls import path
from .views import ReservationCreateView

urlpatterns = [
    path("reservierungen/", ReservationCreateView.as_view(), name="reservation-create"),
]