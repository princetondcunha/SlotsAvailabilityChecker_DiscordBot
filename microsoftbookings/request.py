'''REST Request'''

import requests
from restsetup import url, headers, payload

def restrequest():
    '''REST Request'''
    response = requests.request(
    "POST", url(), headers=headers(), data=payload(), timeout=10)
    return response
