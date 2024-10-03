# serializers.py
from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    soil_temp = serializers.FloatField()
    soil_ph = serializers.FloatField()
