'''Discord Bot'''

import os
import json
import dotenv
import discord
from discord.ext import commands
from request import restrequest

dotenv.load_dotenv()
discord_token = os.environ.get('DISCORD_TOKEN')

intents = discord.Intents.default()

# Create a bot instance
bot = commands.Bot(command_prefix='!',intents=intents)
intents.message_content = True

# Bot event: When the bot is ready
@bot.event
async def on_ready():
    '''On Ready'''
    print(f'Logged in as {bot.user.name}')

# Bot command: A simple command that replies to a specific message
@bot.command()
async def hello(ctx):
    '''Hello'''
    await ctx.send('Hello, world!')

@bot.command()
async def check_bookings(ctx):
    '''Check Microsoft Bookings'''
    response = restrequest()
    data = json.loads(response.text)

    if 'items' in data:
        await ctx.send("Slots available")
    else:
        await ctx.send("No slots")

# Run the bot using your token
bot.run(discord_token)