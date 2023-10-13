'''Process Payload'''

from datetime import datetime, timedelta
import pytz
from tabulate import tabulate


def gettimezone():
    '''Get Timezone'''
    current_timezone = pytz.timezone("America/Halifax")
    return current_timezone


def getdate():
    '''Get Current Date'''
    current_date = datetime.now(tz=gettimezone()).date()
    return current_date

def checkslots(data):
    '''Check Available Slots'''
    appointments = data['StaffBookabilities'][0]['BookableTimeBlocks']

    slots = 0

    for block in appointments:
        start_date_str = block["Start"]
        start_date = datetime.fromisoformat(
            start_date_str).astimezone(gettimezone()).date()
        if start_date >= getdate():
            slots += 1
    return slots

def printslots(data):
    '''Print Available Slots'''
    bookable_time_blocks = data["StaffBookabilities"][0]["BookableTimeBlocks"]
    table = []

    current_date = getdate()

    for time_block in bookable_time_blocks:
        start_time = datetime.fromisoformat(time_block["Start"]).date()
        start_datetime = datetime.fromisoformat(time_block["Start"])

        if start_time >= current_date:
            end_datetime = datetime.fromisoformat(time_block["End"])
            current_datetime = start_datetime
            while current_datetime < end_datetime:
                time_slot_str = current_datetime.strftime("%I:%M %p, %B %d, %Y")
                table.append([time_slot_str])
                current_datetime += timedelta(minutes=10)

    headers = ["Available Time Slots"]
    slottable=tabulate(table, headers, tablefmt="grid",stralign="center")
    return slottable
