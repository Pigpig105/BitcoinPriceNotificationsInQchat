import requests

from chat import headers
from chat import response

url = "http://localhost:12391/chat/compute"

rawtx58 = response

computed = requests.post(url, headers=headers, data=rawtx58)

if computed.status_code == 200:
    print("POST request successful!")
    print("Response:")
    print(computed.text)
else:
    print(f"POST request failed with status code: {computed.status_code}")
    print("Response:")
    print(computed.text)