import requests
import json

from groundfloor import privateKey
from chat import headers
from compute import computed

url = "http://localhost:12391/transactions/sign"

payload = {
    "privateKey": privateKey,
    "transactionBytes": computed
}

json_payload = json.dumps(payload)

signed = requests.post(url, data=json_payload)

if signed.status_code == 200:
    print("POST request successful!")
    print("Response:")
    print(signed.text)
else:
    print(f"POST request failed with status code: {signed.status_code}")
    print("Response:")
    print(signed.text)