from django.contrib import admin

from .models import Resident, Room, Tenancy

admin.site.register(Room)
admin.site.register(Resident)
admin.site.register(Tenancy)
