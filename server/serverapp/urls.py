# urls.py
from django.urls import path
from .views import ColumnNamesView, PlantTypePredictionView

urlpatterns = [
    path('get_column_names/', ColumnNamesView.as_view(), name='get_column_names'),
    path('predict_plant_type/', PlantTypePredictionView.as_view(), name='predict_plant_type'),
]
