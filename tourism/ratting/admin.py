from django.contrib import admin
from .models import Ratting


@admin.register(Ratting)
class RattingAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'created')
    search_fields = ('comment',)
    date_hierarchy = 'created'
