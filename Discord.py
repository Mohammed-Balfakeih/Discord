import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


chat_filter = ['FUCK','SHIT',]
bypass_list = ['347413906613862400']

@client.event
async def on_ready():
    print("Bot is online and connected")
    

@client.event
async def on_message(message):
    # Chat filter
    contents = message.content.split(" ")
    for word in contents:
        #await client.send_message(message.channel, "Help me, I want to live")
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.delete_message(message)
                    await client.send_message(message.channel, "I am sorry, your sentence was very inappropriate and has been deleted")
                except discord.errors.NotFound:
                    return
                   
    if message.content.upper().startswith('!SAY'):
        if message.author.id =='347413906613862400':
            args = message.content.split(' ')
            await client.send_message(message.channel, "%s" % (' '.join(args[1:])))
        else:
            await client.send_message(message.channel, "You are not the ultimate goat, I shall not obey your commands")

    if message.content.upper().startswith('!AMIGOAT'):
        if '461073413491130385' in [role.id for role in message.author.roles]:
            await client.send_message(message.channel, 'You are a goat')
        else:
            await client.send_message(message.channel, 'You are a fake arab')

    
    if message.author.id == '323099913611247617':
        await client.send_message(message.channel, 'VODKA VODKA VODKA, GIVE ME VODKA')

client.run('NDYwOTAxMDgwMjkzNzAzNjkx.DhLjKQ.ALExy2ggG_v1qXDI_kJ4QbG3TP8')




