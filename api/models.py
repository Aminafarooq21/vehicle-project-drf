from django.db import models
from django.contrib.auth.models import User


class Owner(models.Model):
    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    speed = models.IntegerField()
    brand = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    owner = models.ForeignKey(Owner, related_name='vehicles', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def management(self):
        return "---management service of vehicle---"


class Bike(Vehicle):
    has_side_car = models.BooleanField(default=False)
    is_electric = models.BooleanField(default=False)

    def management(self):
        return "---management service of bike---"


class Car(Vehicle):
    is_automatic = models.BooleanField(default=False)

    def management(self):
        return "---management service of car---"


class Bus(Vehicle):
    number_of_decks = models.IntegerField()

    def management(self):
        return "---management service of bus---"
