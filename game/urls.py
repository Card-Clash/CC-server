from django.urls import path

from .views.player import PlayerProfileByIDView, PlayerCards, PlayerProfileByDiscordView
from .views.discord import exchange_token

urlpatterns = [
    path('token', exchange_token, name='exchange_token'),
    path('player/<int:player_id>/profile', PlayerProfileByIDView.as_view(), name='player_data'),
    path('player/discord/<int:discord_id>/profile', PlayerProfileByDiscordView.as_view(), name='player_data'),
    path('player/<int:player_id>/cards', PlayerCards.as_view(), name='player_cards'),
]
