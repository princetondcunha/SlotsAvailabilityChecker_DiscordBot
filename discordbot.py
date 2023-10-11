'''Discord Bot'''

import discord
from discord.ext import commands

# Create a bot instance
bot = commands.Bot(command_prefix='!')

# Bot event: When the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Bot command: A simple command that replies to a specific message
@bot.command()
async def hello(ctx):
    await ctx.send('Hello, world!')

# Run the bot using your token
bot.run("YOUR_BOT_TOKEN")
