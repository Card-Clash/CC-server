from django.urls import path
from .views import exchange_token

urlpatterns = [
    path('api/token', exchange_token, name='exchange_token'),
]
