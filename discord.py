from attr import NOTHING
import api
from pypresence import Presence
import time
from importlib import reload
import json

# Loading the config file
with open('config.json', 'r') as f:
    config = json.load(f)

# Discord client ----------------------------------------------------
client_id = config['id']
RPC = Presence(client_id)
RPC.connect()

# Seting the RPC
while True:
        reload(api)
        print("API Refreshed")
        RPC.update(
        large_image="largeimage",
        large_text="Powerd by Hydisc.tk",
        details=api.detailstatus,
        state=f"{api.ign}"
    )
        time.sleep(60)
        
        
