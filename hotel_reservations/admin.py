from django.contrib import admin
from hotel_reservations import models

admin.site.register(models.Country)
admin.site.register(models.Hotel)
admin.site.register(models.Room)
