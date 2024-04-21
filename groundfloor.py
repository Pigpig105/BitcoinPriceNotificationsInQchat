import requests
from get_bitcoin_price import price

apikey = "Sensitive Info" # Fixme

# Pulls timestamp
# Can be accessed as timestamp.json()
timestampUrl = "http://localhost:12391/utils/timestamp"
timestamp = requests.get(timestampUrl)

# Pulls lastReference
# Can be accessed as reference.json()
referenceUrl = "http://localhost:12391/addresses/lastreference/Qh3qSeUxuF23EaRm5r1p9Nn1ubY8QNGhrt"
reference = requests.get(referenceUrl)

fee = "0.001" # Fixme May need to change to 0.01

txGroupId = "227"

recipient = "0"

senderPublicKey = "5YRwJfycsX8dEP69rR9NetzDGRqPkxDFF9MDChqosvoK"

chatReference = "0"

# Message that gets sent in Qchat
message = "Bitcoin's Price: "+price+" as of 17:30 EST"
data = message

isText = "true"

isEncrypted = "true"

privateKey = "A9MNsATgQgruBUjxy2rjWY36Yf19uRioKZbiLFT2P7c6" #Fixme