import requests
from requests.auth import HTTPBasicAuth
import json

from env import config


def identifySpace():
    url = "https://webexapis.com/v1/rooms"
    payload = None

    header= {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config['WEBEX_ACCESS_TOKEN']}"
    }

    response = requests.request('GET', url, headers=header, data=payload)
    response_txt = response.text.encode('utf8')
    #print(response_txt)
    response_txt2 = json.loads(response_txt)
    
    #print(response_txt2["items"])

    
    for name in response_txt2["items"]:
        if (name["title"] == "CSAP Programmability CTF - Team 2"):
            print(name["id"])
    


#"CSAP Programmability CTF - Team 2"


identifySpace()