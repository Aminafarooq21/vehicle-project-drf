from rest_framework import serializers
from api.models import Car, Vehicle, Bus, Bike, Owner
from django.contrib.auth.models import User


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'name', 'price', 'brand', 'speed', 'colour']

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("PRICE MUST BE POSITIVE")
        return value


class OwnerSerializer(serializers.ModelSerializer):
    vehicles = VehicleSerializer(many=True, read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Owner
        fields = ['user', 'id', 'name', 'contact', 'vehicles']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id',  'name', 'price', 'brand', 'speed', 'colour', 'is_automatic', 'owner']


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = ['id', 'name', 'price', 'brand', 'speed', 'colour', 'has_side_car', 'is_electric', 'owner']

    def validate(self, attrs):
        side_car = attrs.get('has_side_car')
        electric = attrs.get('is_electric')

        if side_car and electric:
            raise serializers.ValidationError("BIKE WITH SIDE CAR CANT BE ELECTRIC")
        return attrs


class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = ['id', 'name', 'price', 'brand', 'speed', 'colour', 'number_of_decks', 'owner']
