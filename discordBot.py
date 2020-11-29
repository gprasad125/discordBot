#Import statements:
    #discord python library
import discord

    #helps with initialization + discord bot functionality
import os
from dotenv import load_dotenv

tokenFile = open('/Users/gokul/discordBot/token.txt')

#load_dotenv()

#find discord token from env file in same area as discordBot.py
token = list(tokenFile)[0]

#initialize client
bot = discord.Client()

#define bot events:
@bot.event
async def sayHello(message):
    if message.content == "Hello":
        await message.channel.send("Hello! I hope you are well")


#run the bot
bot.run(token)
