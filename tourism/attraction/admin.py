from django.contrib import admin

from .models import Attraction


@admin.register(Attraction)
class AttractionAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'description', 'opening_hours', 'min_age')
    search_fields = ('name', 'description')
