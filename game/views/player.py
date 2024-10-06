from json import loads

from asgiref.sync import sync_to_async
from django.http import JsonResponse
from django.views import View

from game.models import Player


class PlayerData(View):
    async def get(self, request):
        player_id = loads(request.body.decode('utf-8')).get('player_id')
        player = await Player.objects.aget(pk=player_id)
        return JsonResponse(player.to_json(), safe=False)


class PlayerCards(View):
    async def get(self, request):
        player_id = loads(request.body.decode('utf-8')).get('player_id')
        player = await Player.objects.aget(pk=player_id)
        player_cards = player.playercard_set.all()
        player_cards_data = await sync_to_async(list)(player_cards.values("card_id", "quantity"))
        return JsonResponse(player_cards_data, safe=False)
