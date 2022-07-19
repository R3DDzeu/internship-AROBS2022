import logging
logging.basicConfig(level=logging.DEBUG)
import asyncio
import simpleobsws
import time

parameters = simpleobsws.IdentificationParameters(ignoreNonFatalRequestChecks = False) # Create an IdentificationParameters object (optional for connecting)

ws = simpleobsws.WebSocketClient(url = 'ws://localhost:4444', password = 'secret', identification_parameters = parameters) # Every possible argument has been passed, but none are required. See lib code for defaults.

async def make_request():
    await ws.connect() # Make the connection to obs-websocket
    await ws.wait_until_identified() # Wait for the identification handshake to complete

    request = simpleobsws.Request('StartRecord') # Build a Request object

    request2 = simpleobsws.Request('StopRecord')

    ret = await ws.call(request) # Perform the request
    time.sleep(121)
    ret2 = await ws.call(request2)
    if ret.ok(): # Check if the request succeeded
        print("Request succeeded! Response data: {}".format(ret.responseData))
    if ret2.ok():  # Check if the request succeeded
         print("Request succeeded! Response data: {}".format(ret2.responseData))

    await ws.disconnect() # Disconnect from the websocket server cleanly

loop = asyncio.get_event_loop()
loop.run_until_complete(make_request())

# pentru a accesa fisierul ne vom folosi de outputPath pt analiza audio + conversie
# mai trebuie facute logurile + estetica