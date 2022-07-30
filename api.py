import json
import requests

# Loading the config file in
with open('config.json', 'r') as f:
    config = json.load(f)


# Key & IGN  /  Variables
key = config['key']
ign = config['ign']

# Requesting the uuid
uuidData = requests.get(f"https://playerdb.co/api/player/minecraft/{ign}").json()
playerUUID = uuidData["data"]["player"]["id"]

# Printing the UUID & IGN
print(f"Player Name: {ign}")
print(f"Player UUID: {playerUUID}")

# Send request and return as json
data = requests.get(f"https://api.hypixel.net/status?key={key}&uuid={playerUUID}").json()

# Getting game type and mode
type1 = data["session"]["gameType"]
mode1 = data["session"]["mode"]

# Editing output
type2 = type1.lower()
mode2 = mode1.lower()
type = type2.capitalize()
mode = mode2.capitalize()
space = " "
status = type + space + mode

# Final Result
print(f"Hypixel {status}")
print("-------------------------------------------------------")

# Needed for RPC
Playing = "Hypixel"
detailstatus = Playing + space + status