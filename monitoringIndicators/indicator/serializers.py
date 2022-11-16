from rest_framework import serializers

from .models import DiodIndicator


class IndicatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiodIndicator
        fields = "__all__"
