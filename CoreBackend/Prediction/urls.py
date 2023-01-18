from django.urls import path
from Prediction.views import PredictView 

urlpatterns = [
    path("",PredictView.as_view(),name="prediction_endpoint")
]
