from led import set_color_hex, colorWipe
from rpi_ws281x import Color
import led_visualizer
import visualization
import asyncio
import websockets
import json
import threading

# https://websockets.readthedocs.io/en/9.0.1/intro.html
async def server(websocket, path):
    try:
        async for message in websocket:
            data = json.loads(message)
            print('new event')
            print(data)
            if data["action"] == "set_color_hex":
                set_color_hex(data["value"])
            else:
                print('action not found')
                
    finally:
      print('server finally')

def visualizer():
  try:
    # Start listening to live audio stream
    visualization.microphone.start_stream(visualization.microphone_update)
  finally:
    print('visualizer finally')

if __name__ == '__main__':
  # thread1 = threading.Thread(target=start_server)
  # thread1.start()
  try: 
    # Initialize visualizer LEDs
    led_visualizer.update()
    thread2 = threading.Thread(target=visualizer)
    thread2.start()

    start_server = websockets.serve(server, "0.0.0.0", 5000)
    asyncio.get_event_loop().run_until_complete(start_server)
    print('starting socket server on ws://0.0.0.0:5000')
    asyncio.get_event_loop().run_forever()

  except KeyboardInterrupt:
    colorWipe(Color(0,0,0), 10)