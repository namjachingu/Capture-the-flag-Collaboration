
import json
import requests

from env import config

headers = {
    'Accept': 'application/json',
    "Authorization": f"Bearer {config['WEBEX_ACCESS_TOKEN']}"
}

def createRoom():
    payload = {"title": "Felicia's magic corner"}
    url = "https://webexapis.com/v1/rooms"
    response = requests.request("POST", url, data=payload, headers=headers)
    response2 = response.json()
    print(response2["id"])
    return response2["id"]

x = createRoom()


def addMembers(user_emails):
    url = "https://webexapis.com/v1/memberships"
    
    for user_email in user_emails:
        payload = {"roomId": x, "personEmail": user_email}
        response = requests.request("POST", url, data=payload, headers=headers)
        print(response)


addMembers(["mneiding@cisco.com", "frewagne@cisco.com"])
#addMembers(["pverhage@cisco.com", "felicia.rahim@gmail.com"])


def sendMessage():
    url = "https://webexapis.com/v1/messages"
    payload = {"roomId": x, "text": ["Hello World"]}
    response = requests.request("POST", url, data=payload, headers=headers)
    response2 = response.json()
    print(response2)

sendMessage()