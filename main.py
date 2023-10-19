'''Discord Bot'''

import os
import json
import sys
import dotenv
import discord
from discord.ext import commands
from request import restrequest
from processpayload import checkslots, printslots

dotenv.load_dotenv()
discord_token = os.environ.get('DISCORD_TOKEN')
channelid = os.environ.get('CHANNEL_ID')

intents = discord.Intents.default()

bot = commands.Bot(command_prefix='!',intents=intents)
intents.message_content = True

@bot.event
async def on_ready():
    '''On Ready'''
    print(f'Logged in as {bot.user.name}')
    channel = bot.get_channel(int(channelid))
    await channel.send(await check_bookings('check_bookings'))
    print("Logged: Shuting Down")
    sys.exit(0)

@bot.command()
async def serverstatus(ctx):
    '''Check Server Status'''
    await ctx.send('Server is up')

@bot.command()
async def check_bookings(ctx):
    '''Check Microsoft Bookings'''
    print("Logged:",ctx)
    response = restrequest()
    data = json.loads(response.text)
    slots = checkslots(data)
    slotstable = printslots(data)

    if slots > 0:
        return "Slots available\n" + slotstable
    else:
        print("Logged: Shuting Down")
        sys.exit(0)

@bot.command()
async def check_bookings_manual(ctx):
    '''Check Microsoft Bookings Manually'''
    response = restrequest()
    data = json.loads(response.text)
    slots = checkslots(data)
    slotstable = printslots(data)

    if slots > 0:
        await ctx.send("Slots available"+slotstable)
    else:
        await ctx.send("No slots")

bot.run(discord_token)
