import pystray
import PIL.Image
from importlib import reload
import os
import webbrowser

# Image for the tray
image = PIL.Image.open("hydisc.png")

# Triggers for right click

def ss(icon, item):
    import discord

def edit(icon, item):
    os.system('config.json')

def git(icon, item):
    webbrowser.open('https://github.com/NeonDevGit/HyDisc')

def support(icon, item):
    webbrowser.open('https://discord.gg/9Q7SBStDef')

# Buttons for right click
icon = pystray.Icon("Hydisc", image, menu=pystray.Menu(
    pystray.MenuItem("Start", ss),
    pystray.MenuItem("Edit Settings", edit),
    pystray.MenuItem("Github", git),
    pystray.MenuItem("Support", support)
))

icon.run()