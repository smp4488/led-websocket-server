# https://python-socketio.readthedocs.io/en/latest/intro.html

from led import set_color_hex, colorWipe
from aiohttp import web
from rpi_ws281x import Color
import sys
import socketio
import threading
import led_visualizer
import visualization

CURRENT_COLOR = None

sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*')
# sio = socketio.Server(async_mode='threading', cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

async def index(request):
    """Serve the client-side application."""
    with open('static/index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
def connect(sid, environ):
    print("connect ", sid)

@sio.event
async def chat_message(sid, data):
    print("message ", data)

@sio.event
def set_color(sid, hex):
    print('set_color ', hex)
    CURRENT_COLOR = hex
    set_color_hex(hex)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

def socket_io_server():
  try:
    # web.run_app(app)
    sio.run(app)
  finally:
    print('socketio finally')

def visualizer(current_color):
  try:
    # Start listening to live audio stream
    visualization.microphone.start_stream(visualization.microphone_update, current_color)
  except KeyboardInterrupt:
    colorWipe(Color(0,0,0), 10)
  finally:
    print('visualizer finally')

if __name__ == '__main__':

  try: 
    # Initialize socketio server
    thread1 = threading.Thread(target=socket_io_server)
    thread1.start()
    
    # Initialize visualizer LEDs
    # led_visualizer.update()
    thread2 = threading.Thread(target=visualizer, args=(CURRENT_COLOR, ))
    thread2.start()

    # web.run_app(app)


  except KeyboardInterrupt:
    colorWipe(Color(0,0,0), 10)
    sys.exit(1)