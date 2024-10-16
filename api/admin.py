from django.contrib import admin
from api.models import Bike, Bus, Vehicle, Car, Owner

admin.site.register(Bus)
admin.site.register(Owner)
admin.site.register(Bike)
admin.site.register(Car)
admin.site.register(Vehicle)
