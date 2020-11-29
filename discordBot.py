#Import statements:
import discord #discord python library

import os #helps with initialization + discord bot functionality
from dotenv import load_dotenv

#load_dotenv()

#find discord token from env file in same area as discordBot.py
#token = os.getenv("DISCORD_TOKEN")

#initialize client
bot = discord.Client()

#define bot events:
@bot.event
async def sayHello(message):
    if message.content == "Hello":
        await message.channel.send("Hello! I hope you are well")


#run the bot
bot.run('NzgyNDE1NzM4MTQ0MDMwNzYw.X8L3cA.SW7mqqrJluV_GB_AAMNO8y0IUAM')
