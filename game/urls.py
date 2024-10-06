from django.urls import path

from .views.player import PlayerData, PlayerCards
from .views.discord import exchange_token

urlpatterns = [
    path('api/token', exchange_token, name='exchange_token'),
    path('api/player_data', PlayerData.as_view(), name='player_data'),
    path('api/player_cards', PlayerCards.as_view(), name='player_cards'),
]
