from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from .serializers import PredictionSerializer

# Load the model when the server starts
models.load_saved_artifacts()

class ColumnNamesView(APIView):
    def get(self, request):
        columns = models.get_data_columns()
        return Response({'columns': columns})

class PlantTypePredictionView(APIView):
    def post(self, request):
        serializer = PredictionSerializer(data=request.data)
        if serializer.is_valid():
            soil_temp = serializer.validated_data['soil_temp']
            soil_ph = serializer.validated_data['soil_ph']
            prediction = models.get_predicted_plant_type(soil_temp, soil_ph)
            return Response({'predicted_plant_type': prediction})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
