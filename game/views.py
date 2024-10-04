from json import loads
from os import environ
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from pip._vendor.requests.models import Response

from game.models import Player


@csrf_exempt
def exchange_token(request):
    if request.method == "POST":
        code = loads(request.body.decode('utf-8')).get('code')

        response = requests.post(
            "https://discord.com/api/oauth2/token",
            headers={
                "Content-Type": "application/x-www-form-urlencoded",
            },
            data={
                "client_id": environ["DISCORD_APP_ID"],
                "client_secret": environ["DISCORD_APP_CLIENT_SECRET"],
                "grant_type": "authorization_code",
                "code": code,
            }
        )

        response_data = response.json()
        access_token = response_data.get("access_token")

        return JsonResponse({"access_token": access_token})
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)


@csrf_exempt
def get_player_data(request):
    if request.method == "POST":
        player_id = loads(request.body.decode('utf-8')).get('player_id')
        player = Player.objects.get(pk=player_id)
        return JsonResponse(player.__dict__())
