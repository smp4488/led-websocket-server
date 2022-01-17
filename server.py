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
    except KeyboardInterrupt:
      colorWipe(Color(0,0,0), 10)
                
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

  # Initialize LEDs
  # led_visualizer.update()
  # thread2 = threading.Thread(target=visualizer)
  # thread2.start()

  start_server = websockets.serve(server, "0.0.0.0", 5000)
  asyncio.get_event_loop().run_until_complete(start_server)
  print('starting socket server on ws://0.0.0.0:5000')
  asyncio.get_event_loop().run_forever()


# import eventlet
# import socketio
# # sio = socketio.Server()
# sio = socketio.Server(cors_allowed_origins=['*'])
# app = socketio.WSGIApp(sio, static_files={
#     '/': {'content_type': 'text/html', 'filename': 'index.html'}
# })

# @sio.event
# def connect(sid, environ):
#     print('connect ', sid)

# @sio.event
# def my_message(sid, data):
#     print('message ', data)

# @sio.event
# def set_color(sid, data):
#     print('set_color ', data)

# @sio.event
# def set_color_hex(sid, data):
#     print('set_color ', data)
#     set_color_hex(data)

# @sio.event
# def get_color(sid, data):
#     print('set_color ', data)

# @sio.event
# def disconnect(sid):
#     print('disconnect ', sid)

# if __name__ == '__main__':
#     eventlet.wsgi.server(eventlet.listen(('', 5000)), app)