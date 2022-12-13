from django.urls import path
from .views import *


urlpatterns = [
    path('user/', UserAPIView.as_view()),
    
]
