#Import statements:
import discord #discord python library

import os #helps with initialization + discord bot functionality
from dotenv import load_dotenv

load_dotenv()

#find discord token from env file in same area as discordBot.py
token = os.getenv("DISCORD_TOKEN")

#initialize client
bot = discord.Client()

#define bot events:
