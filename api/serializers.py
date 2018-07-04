"""Serializers module to conver JSON to HTTP request and back."""

from rest_framework import serializers
from .models import Currency

class CurrencySerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Currency
        fields = ('id', 'symbol', 'date_created', 'ecb_rate')
        read_only_fields = ('date_created', 'id')