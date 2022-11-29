from django.urls import path
from Prediction.views import index 

urlpatterns = [
    path("",index)
]
