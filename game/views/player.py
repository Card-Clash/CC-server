from json import loads

from django.http import JsonResponse
from django.views import View

from game.models import Player


class PlayerData(View):
    def get(self, request):
        player_id = loads(request.body.decode('utf-8')).get('player_id')
        player = Player.objects.get(pk=player_id)
        return JsonResponse(player.to_json(), safe=False)


class PlayerCards(View):
    def get(self, request):
        player_id = loads(request.body.decode('utf-8')).get('player_id')
        player = Player.objects.get(pk=player_id)
        player_cards = player.playercard_set.all()
        return JsonResponse(list(player_cards.values("card_id", "quantity")), safe=False)
