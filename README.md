The purpose of this repository is to provide a rather useful alert to all crypto inclined Qortians.  Additionally this is a personal project to better my skills in programming.

Here is the project breakdown.  This program will send a chat message in Qortal's Q-Chat every 24 hours saying "Bitcoin's Price: $65,178.79 as of 17:30 EST".  This is sent in the "announcements group"

The code will pull bitcoin's price from coinmarketcap.com with http requests, and parsing html (get_bitcoin_price.py).  It will than pull a buncha good stuff from the Qortal Core using GET API's to start building the groundfloor (groundfloor.py)  The next few py files will build the tx.

The Order of Operations for APIs in Qortal for building a successful tx to get published is as follows:

1. /chat
2. /chat/compute
3. /transactions/sign
4. /transactions/process

Each one of these stages has its own file in the code.

THIS IS CURRENTLY NOT WORKING, NOR HAS IT EVER BEEN EXECUTED.  THIS PROJECT IS STILL IN BETA STAGE.
