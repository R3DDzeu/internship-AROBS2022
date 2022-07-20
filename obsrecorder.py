import logging
logging.basicConfig(level=logging.DEBUG)
import asyncio
import simpleobsws

pth2 = None
parameters = simpleobsws.IdentificationParameters(ignoreNonFatalRequestChecks = False) # Create an IdentificationParameters object (optional for connecting)

ws = simpleobsws.WebSocketClient(url = 'ws://localhost:4444', password = 'secret', identification_parameters = parameters) # Every possible argument has been passed, but none are required. See lib code for defaults.

async def make_request():
    global pth2
    await ws.connect() # Make the connection to obs-websocket
    await ws.wait_until_identified() # Wait for the identification handshake to complete

    request = simpleobsws.Request('StartRecord') # Build a Request object

    request2 = simpleobsws.Request('StopRecord')

    ret = await ws.call(request) # Perform the request
    await asyncio.sleep(20)
    ret2 = await ws.call(request2)
    if ret.ok(): # Check if the request succeeded
        print("Request succeeded! Response data: {}".format(ret.responseData))
    if ret2.ok():  # Check if the request succeeded
        print("Request succeeded! Response data: {}".format(ret2.responseData))

    if 'outputPath' in ret2.responseData:
        pth = ret2.responseData['outputPath']
        if ".mov" in pth:
            pth2=pth
    await ws.disconnect() # Disconnect from the websocket server cleanly

def startrec():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(make_request())

def getPth2():
    global pth2
    return pth2



#conversie  + analiza audio
#estetica
#update documentatie OBS !!!!!!!!! + comentarii
# pip install pip install ffmpeg moviepy in documentatie !!!!!!! (pentru conversie)