'''Slots Availability Checker - Python'''

import json
import os
import requests
import dotenv

dotenv.load_dotenv()
staff_list_value = os.environ.get('STAFF_LIST')
serviceid_value = os.environ.get('SERVICEID')
user_identity_value = os.environ.get('USER_IDENTITY')

URL = f"https://outlook.office365.com/owa/calendar/{user_identity_value}/bookings/service.svc/GetStaffBookability"

payload = json.dumps({
  "StaffList": [staff_list_value],
  "Start": "2023-10-07T00:00:00",
  "End": "2023-11-02T00:00:00",
  "TimeZone": "America/Halifax",
  "ServiceId": serviceid_value
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", URL, headers=headers, data=payload, timeout=10)

slots = json.loads(response.text)["StaffBookabilities"][0]["BookableTimeBlocks"]

slots_count=len(slots)

if slots_count>0:
    print("Slots Available :",slots_count)
else:
    print("No slots available")