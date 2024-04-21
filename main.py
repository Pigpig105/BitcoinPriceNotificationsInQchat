import requests

from sign import signed

url = "http://localhost:12391/transactions/process"

headers = {
    "accept: text/plain",
    "X-API-VERSION: 1",
    "Content-Type: application/json"
}

processed = requests.post(url, headers=headers, data=signed)

if processed.status_code == 200:
    print("POST request successful!")
    print("Response:")
    print(processed.text)
else:
    print(f"POST request failed with status code: {processed.status_code}")
    print("Response:")
    print(processed.text)