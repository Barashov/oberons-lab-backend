from django.urls import path
from .views import *


urlpatterns = [
    path('user/', UserAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view()),
    path('is_auth/', is_auth_view),
    path('is_email_taken/<email>/', is_email_taken_view)
]
