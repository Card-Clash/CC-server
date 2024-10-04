from os import environ

import requests

url = f"https://discord.com/api/v10/applications/{environ["DISCORD_APP_ID"]}/commands"
headers = {
    "Authorization": "Bot " + environ["DISCORD_APP_TOKEN"],
    "Content-Type": "application/json"
}
data = {
    "name": "launch",
    "description": "Launch Card Clash",
    "type": 4,
    "handler": 2
}

try:
    response = requests.post(url, headers=headers, json=data)
except requests.exceptions.ConnectionError:
    response = requests.Response()
    response.status_code = 500

if response.status_code == 200:
    print("Entry Command Registered")
else:
    print("Entry Command NOT Registered")
