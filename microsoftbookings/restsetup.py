'''REST Request Setup'''

import os
import json
import dotenv

dotenv.load_dotenv()

staff_list_value = os.environ.get('STAFF_LIST')
serviceid_value = os.environ.get('SERVICEID')
user_identity_value = os.environ.get('USER_IDENTITY')

def url():
    '''Form URL'''
    urlform = "https://outlook.office365.com/owa/calendar/"
    urlform+= user_identity_value
    urlform+= "/bookings/service.svc/GetStaffBookability"
    return urlform

def headers():
    '''Form Headers'''
    headersform = {
        "Content-Type":"application/json"
    }
    return headersform

def payload():
    '''Form Payload'''
    payloadform = json.dumps({
    "StaffList": [staff_list_value],
    "Start": "2023-01-01T00:00:00",
    "End": "2025-01-01T00:00:00",
    "TimeZone": "America/Halifax",
    "ServiceId": serviceid_value
    })
    return payloadform
