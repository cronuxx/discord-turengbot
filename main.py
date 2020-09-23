import discord
import os

from discord.ext import commands

client = commands.Bot(command_prefix='.')
TOKEN = 'your token here'

@client.event
async def on_ready():
    print('Bot is ready...')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run(TOKEN)
