'''Discord Bot'''

import os
import json
import dotenv
import requests
import discord
from discord.ext import commands

dotenv.load_dotenv()
discord_token = os.environ.get('DISCORD_TOKEN')
staff_list_value = os.environ.get('STAFF_LIST')
serviceid_value = os.environ.get('SERVICEID')
user_identity_value = os.environ.get('USER_IDENTITY')

URL = "https://outlook.office365.com/owa/calendar/"
URL+= user_identity_value
URL+= "/bookings/service.svc/GetStaffBookability"

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
    payload = json.dumps({
    "StaffList": [staff_list_value],
    "Start": "2023-01-01T00:00:00",
    "End": "2025-01-01T00:00:00",
    "TimeZone": "America/Halifax",
    "ServiceId": serviceid_value
    })
    headers = {
        "Content-Type":"application/json"
    }
    response = requests.request(
    "POST", URL, headers=headers, data=payload, timeout=10)
    data = json.loads(response.text)

    if 'items' in data:
        await ctx.send("Slots available")
    else:
        await ctx.send("No slots")

# Run the bot using your token
bot.run(discord_token)
