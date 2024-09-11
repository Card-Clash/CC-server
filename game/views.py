from json import loads
from os import environ
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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
