'''Discord Bot'''

import os
import discord
from discord.ext import commands
import dotenv

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

# Run the bot using your token
bot.run(discord_token)
