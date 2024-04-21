import requests
import json

from groundfloor import apikey
from groundfloor import timestamp
from groundfloor import reference
from groundfloor import fee
from groundfloor import txGroupId
from groundfloor import recipient
from groundfloor import senderPublicKey
from groundfloor import chatReference
from groundfloor import data
from groundfloor import isText
from groundfloor import isEncrypted

url = "http://localhost:12391/chat"

headers = {
    "accept: text/plain",
    "X-API-KEY: "+apikey,
    "Content-Type: application/json"
}

payload = {
    "timestamp": timestamp,
    "reference": reference,
    "fee": fee,
    "txGroupId": txGroupId,
    "recipient": recipient,
    "senderPublicKey": senderPublicKey,
    "chatReference": [
        chatReference
    ],
    "data": data,
    "isText": isText,
    "isEncrypted": isEncrypted
}

json_payload = json.dumps(payload)

response = requests.post(url, headers=headers, data=json_payload)

if response.status_code == 200:
    print("POST request successful!")
    print("Response:")
    print(response.json())  # Assuming the response is in JSON format
else:
    print(f"POST request failed with status code: {response.status_code}")
    print("Response:")
    print(response.text)  # Print response content for error debugging