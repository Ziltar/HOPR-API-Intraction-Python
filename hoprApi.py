import requests
import json

NODE_URL = "" 
API_KEY = ""
NODE_HOPR_ADR = ""

def sendRequest(method, path, payload):
    global NODE_URL, API_KEY
    url = NODE_URL +  path

    payload = json.dumps(payload)
    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'x-auth-token': API_KEY
    }

    response = requests.request(method, url, headers=headers, data=payload)
    return(response.json())

def ping(peerId):
    return (sendRequest("POST","/api/v2/node/ping", payload = {
        "peerId": peerId
    }))

def openChannel(peerId, amount):
    return(sendRequest("POST","/api/v2/channels/",   payload = {
        "peerId": peerId,
        "amount": str(int(amount*1000000000000000000))
    }))    

def close_Channel(peerId):
    return(sendRequest("DELETE", "/api/v2/channels/"+peerId+"/outgoing/", {}))

def get_peers():
    return (sendRequest("GET","/api/v2/node/peers", {}),)   

def send_message(msg_to, msg, msg_path):
    return(sendRequest("POST", "/api/v2/messages/", {
        "body": msg,
        "recipient": msg_to,
        "path": msg_path
        }))    
