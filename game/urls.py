from django.urls import path

from .views.player import PlayerData, PlayerCards
from .views.discord import exchange_token

urlpatterns = [
    path('api/token', exchange_token, name='exchange_token'),
    path('api/get_player_data', PlayerData.as_view(), name='get_player_data'),
    path('api/get_player_cards', PlayerCards.as_view(), name='get_player_cards'),
]
