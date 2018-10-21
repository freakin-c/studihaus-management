from django.contrib import admin

from .models import Resident, Room

admin.site.register(Room)
admin.site.register(Resident)
