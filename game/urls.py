from django.urls import path
from .views import exchange_token, get_player_data, get_player_card

urlpatterns = [
    path('api/token', exchange_token, name='exchange_token'),
    path('api/get_player_data', get_player_data, name='get_player_data'),
    path('api/get_player_card', get_player_card, name='get_player_card'),
]
