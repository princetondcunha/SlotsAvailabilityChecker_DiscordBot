'''Discord Bot Version.Chronos'''

import asyncio
import os
import json
import sys
import threading
import dotenv
import discord
from discord.ext import commands
from request import restrequest
from processpayload import checkslots, printslots

def timeguard():
    '''The Timeguard'''
    print("Shutting down")
    sys.exit()

timer = threading.Timer(60,timeguard)
timer.start()

timer.join()

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

    async def background_task():
        while True:
            response_str = await check_bookings('check_bookings')

            if response_str is not None:
                try:
                    await channel.send(response_str)
                except discord.errors.HTTPException:
                    for chunks in response_str.split("+-----------------------------+")[:-1]:
                        await channel.send(chunks+"+-----------------------------+\n")
                await asyncio.sleep(900)
            else:
                await asyncio.sleep(60)

    bot.loop.create_task(background_task())

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

    try:
        if data != dataprev:
            dataprev = data
            if slots > 0:
                return "Slots available\n" + slotstable
    except UnboundLocalError:
        dataprev = data
        if slots > 0:
            return "Slots available\n" + slotstable

    dataprev = data

@bot.command()
async def check_bookings_manual(ctx):
    '''Check Microsoft Bookings Manually'''
    response = restrequest()
    data = json.loads(response.text)
    slots = checkslots(data)
    slotstable = printslots(data)

    if slots > 0:
        await ctx.send("Slots available",slotstable)
    else:
        await ctx.send("No slots")

bot.run(discord_token)
