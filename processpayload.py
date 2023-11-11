'''Process Payload'''

from datetime import datetime, timedelta
import pytz
from tabulate import tabulate


def gettimezone():
    '''Get Timezone'''
    return "America/Halifax"

def getdatetime():
    '''Get Current Date Time'''
    current_datetime = datetime.now(pytz.timezone(gettimezone()))
    return current_datetime

def round10min(dt):
    '''Round the datetime to 10th minute'''
    rounded_minute = (dt.minute // 10) * 10
    rounded_dt = dt.replace(minute=rounded_minute, second=0, microsecond=0)
    return rounded_dt

def checkslots(data):
    '''Check Available Slots'''
    appointments = data['StaffBookabilities'][0]['BookableTimeBlocks']

    slots = 0
    current_datetime = getdatetime()

    for block in appointments:
        start_date_str = block["Start"]
        end_date_str = block["End"]
        start_datetime = datetime.fromisoformat(
            start_date_str).astimezone(pytz.timezone(gettimezone()))
        end_datetime = datetime.fromisoformat(
            end_date_str).astimezone(pytz.timezone(gettimezone()))
        if start_datetime >= current_datetime:
            slots += 1
        elif start_datetime < current_datetime and end_datetime > current_datetime:
            slots += 1

    return slots

def printslots(data):
    '''Print Available Slots'''
    bookable_time_blocks = data["StaffBookabilities"][0]["BookableTimeBlocks"]
    table = []

    current_datetime = getdatetime()

    for time_block in bookable_time_blocks:
        start_datetime = datetime.fromisoformat(time_block["Start"])
        end_datetime = datetime.fromisoformat(time_block["End"])
        if start_datetime >= current_datetime:
            current_datetime = start_datetime
            while current_datetime < end_datetime:
                time_slot_str = current_datetime.strftime("%I:%M %p, %B %d, %Y")
                table.append([time_slot_str])
                current_datetime += timedelta(minutes=10)
        elif start_datetime < current_datetime and end_datetime > current_datetime:
            rcurrent_datetime = round10min(current_datetime)
            if rcurrent_datetime!=current_datetime:
                current_datetime += timedelta(minutes=10)
                rcurrent_datetime += timedelta(minutes=10)
            while current_datetime < end_datetime:
                time_slot_str = rcurrent_datetime.strftime("%I:%M %p, %B %d, %Y")
                table.append([time_slot_str])
                current_datetime += timedelta(minutes=10)
                rcurrent_datetime += timedelta(minutes=10)

    headers = ["Available Time Slots"]
    slottable=tabulate(table, headers, tablefmt="grid",stralign="center")
    return slottable
