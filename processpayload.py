'''Process Payload'''

import datetime
import pytz


def gettimezone():
    '''Get Timezone'''
    current_timezone = pytz.timezone("America/Halifax")
    return current_timezone


def getdate():
    '''Get Current Date'''
    current_date = datetime.datetime.now(tz=gettimezone()).date()
    return current_date

def checkslots(data):
    '''Check Available Slots'''
    appointments = data['StaffBookabilities'][0]['BookableTimeBlocks']

    slots = 0

    for block in appointments:
        start_date_str = block["Start"]
        start_date = datetime.datetime.fromisoformat(
            start_date_str).astimezone(gettimezone()).date()
        if start_date >= getdate():
            slots += 1
    return slots
