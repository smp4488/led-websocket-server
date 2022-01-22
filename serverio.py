# https://python-socketio.readthedocs.io/en/latest/intro.html

from led import set_color_hex, colorWipe
from aiohttp import web
from rpi_ws281x import Color
import logger
# import logging
import sys
import asyncio
import socketio
import threading
import led_visualizer
import visualization

# logger = logging.getLogger('root')

import logging
from logging.handlers import RotatingFileHandler

log_formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s(%(lineno)d) %(message)s')

logFile = '/var/log/serverio.log'

my_handler = RotatingFileHandler(logFile, mode='a', maxBytes=5*1024*1024, 
                                 backupCount=2, encoding=None, delay=0)
my_handler.setFormatter(log_formatter)
my_handler.setLevel(logging.INFO)

logger = logging.getLogger('root')
logger.setLevel(logging.INFO)

logger.addHandler(my_handler)


CURRENT_COLOR = None

sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*', logger=logger)
# sio = socketio.Server(async_mode='threading', cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

# async def index(request):
#     """Serve the client-side application."""
#     with open('static/index.html') as f:
#         return web.Response(text=f.read(), content_type='text/html')

@sio.event
async def connect(sid, environ):
    global CURRENT_COLOR
    logger.info("connect " + sid)
    # print("current color", CURRENT_COLOR)
    await sio.emit('set_color', CURRENT_COLOR)

@sio.event
async def set_color(sid, hex):
    global CURRENT_COLOR
    logger.info('set_color ' + hex)
    CURRENT_COLOR = hex
    set_color_hex(hex)
    await sio.emit('set_color', hex)

@sio.event
def disconnect(sid):
    logger.info('disconnect ' + sid)

# app.router.add_static('/static', 'static')
# app.router.add_get('/', index)

# def socket_io_server(runner):
#   try:
#     # web.run_app(app)
#     # sio.run(app)
#     loop = asyncio.new_event_loop()
#     asyncio.set_event_loop(loop)
#     loop.run_until_complete(runner.setup())
#     site = web.TCPSite(runner, 'localhost', 8080)
#     loop.run_until_complete(site.start())
#     loop.run_forever()
#   finally:
#     print('socketio finally')

def visualizer(current_color):
  try:
    # Start listening to live audio stream
    visualization.microphone.start_stream(visualization.microphone_update, current_color)
  except KeyboardInterrupt:
    colorWipe(Color(0,0,0), 10)
  finally:
    logger.info('visualizer finally')

if __name__ == '__main__':

  try: 
    # Initialize socketio server
    # runner = web.AppRunner(app)
    # thread1 = threading.Thread(target=socket_io_server, args=(runner, ))
    # thread1.start()
    
    # Initialize visualizer LEDs
    # led_visualizer.update()
    # thread2 = threading.Thread(target=visualizer, args=(CURRENT_COLOR, ))
    # thread2.start()

    web.run_app(app)


  except KeyboardInterrupt:
    colorWipe(Color(0,0,0), 10)
    sys.exit(1)