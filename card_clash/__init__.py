from os import environ

import requests
from dotenv.main import load_dotenv

load_dotenv()
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

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    print("Entry Command Registered")
else:
    print("Entry Command Not Registered")
