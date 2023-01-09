from rest_framework import serializers
from .models import Country

class Countryerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('pk','county_name', 'city', 'currency', 'owner')