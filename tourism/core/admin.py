from django.contrib import admin

from .models import TouristSpot


@admin.register(TouristSpot)
class TouristSpotAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'description', 'approved')
    search_fields = ('name', 'description')
    list_filter = ('approved',)
