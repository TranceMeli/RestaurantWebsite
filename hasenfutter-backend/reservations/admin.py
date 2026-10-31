from django.contrib import admin
from .models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ["name", "date", "time", "guests", "email", "created_at"]
    list_filter = ["date"]
    search_fields = ["name", "email"]