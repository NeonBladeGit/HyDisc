import requests
from tkinter import *
import json
from pprint import pprint


def getInfo(call):
    r = requests.get(call)
    return r.json()


# --------------------------------------------------
# Fetching the config file
with open('config.json', 'r') as f:
    config = json.load(f)
    
user_uuid = config['user_uuid']
token = config['token']
# --------------------------------------------------
# Some simple Tkinter for the window
ws=Tk()
ws.geometry("200x100")
# --------------------------------------------------
#Settings are below (are edited threw the config)

uuid_value = user_uuid

API_KEY = token

#------------------------------------------------------------------------------
#Importing the api to the program
uuid_link = f"https://api.hypixel.net/status?key={API_KEY}&uuid={uuid_value}"
url = f"https://api.hypixel.net/status?key={API_KEY}&uuid={uuid_value}"

data = getInfo(url)

# ----------------------------------------------------------------------------------
#Grabing the infortmation from the api, then adding the values together to make one
Value1 = data["session"]["gameType"]
Value2 = data["session"]["mode"]
Value3 = ' / '
print(Value1)
print(Value2)
Value =  Value1 + Value3 + Value2
# -----------------------------------------
# Some simple Tkinter for the window
ws.title(Value.lower())
ws.mainloop()
# -----------------------------------------