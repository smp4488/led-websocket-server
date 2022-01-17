from led import set_color_hex

import asyncio
import websockets
import json

async def server(websocket, path):
    # register(websocket) sends user_event() to websocket
    # await register(websocket)
    try:
        # await websocket.send(state_event())
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "set_color_hex":
                set_color_hex(data['value'])
                # STATE["value"] -= 1
                # await notify_state()
            elif data["action"] == "plus":
              print('action not found')
                # STATE["value"] += 1
                # await notify_state()
            else:
                print('action not found')
                # logging.error("unsupported event: %s", data)
                
    finally:
      print('finally')
        # await unregister(websocket)

if __name__ == '__main__':
  start_server = websockets.serve(server, "localhost", 5000)
  asyncio.get_event_loop().run_until_complete(start_server)
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