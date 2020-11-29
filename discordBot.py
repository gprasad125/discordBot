#Import statements (discord + discord commands modules):
import discord
from discord.ext import commands

#load a token from a file and assign
tokenFile = open('/Users/gokul/token.txt')
token = list(tokenFile)[0]

#initialize client + prefix for commands
bot = commands.Bot(command_prefix = "*")

#define bot events:
@bot.event
async def sayHello(message):
    if message.content == "Hello!":
        await message.channel.send("Hello! I hope you are well")

#run the bot
bot.run(token)
