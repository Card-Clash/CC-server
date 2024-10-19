from json import loads

from django.http import JsonResponse
from django.views import View

from game.models import Player


class PlayerProfileByIDView(View):
    def get(self, request, player_id: int):
        player = Player.objects.get(pk=player_id)
        return JsonResponse(player.to_json(), safe=False)


class PlayerProfileByDiscordView(View):
    def get(self, request, discord_id):
        player = Player.objects.get(discord_id=discord_id)
        return JsonResponse(player.to_json(), safe=False)


class PlayerCards(View):
    def get(self, request, player_id: int):
        player = Player.objects.get(pk=player_id)
        player_cards = player.playercard_set.all()
        return JsonResponse(list(player_cards.values("card_id", "quantity")), safe=False)
