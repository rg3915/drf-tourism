from django.contrib import admin

from .models import Document, TouristSpot


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('__str__',)
    search_fields = ('description',)


@admin.register(TouristSpot)
class TouristSpotAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'description', 'approved')
    search_fields = ('name', 'description')
    list_filter = ('approved',)
