# https://python-socketio.readthedocs.io/en/latest/intro.html

from led import set_color_hex, colorWipe
from aiohttp import web
# from rpi_ws281x import Color
from pathlib import Path
import logger
import logging
import sys
import signal
# import asyncio
import socketio
# import threading
# import led_visualizer
import visualization
from effects.manager import EffectsManager

logger = logging.getLogger()
script_location = Path(__file__).absolute().parent

CURRENT_COLOR = '#000000'

sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*', logger=logger)
# sio = socketio.Server(async_mode='threading', cors_allowed_origins='*')
app = web.Application()
sio.attach(app)

effects = EffectsManager()

async def index(request):
    """Serve the client-side application."""
    with open(script_location / 'static/index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

@sio.event
async def connect(sid, environ):
    global CURRENT_COLOR
    logger.info("connect " + sid)
    logger.info("current color " + CURRENT_COLOR)
    await sio.emit('set_color', CURRENT_COLOR, room = sid)
    data = [effect.toJSON() for effect in effects.effects]
    await sio.emit('get_effects', data, room = sid)

@sio.event
async def set_color(sid, hex):
    global CURRENT_COLOR
    logger.info('set_color ' + hex)
    logger.info('current color ' + CURRENT_COLOR)
    CURRENT_COLOR = hex
    set_color_hex(hex)
    await sio.emit('set_color', hex)

@sio.event
async def set_effect(sid, data):
  logger.info('set effect ' + data['name'])
  effects.set_effect(data['name'], data['options'])
  sio.start_background_task(effects.set_effect, data['name'], data['options'])
  sio.sleep(1)

@sio.event
async def get_effects(sid):
  logger.info('get_effects')
  sio.emit(effects.get_effects(), room = sid)

@sio.event
def disconnect(sid):
    logger.info('disconnect ' + sid)

app.router.add_static('/assets', script_location / 'static/assets')
app.router.add_get('/', index)

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
    logger.warning('Keyboard interrupt (SIGINT) received...')
    # colorWipe(Color(0,0,0), 10)
  finally:
    logger.info('visualizer finally')

def handler_stop_signals(signum, frame):
  logger.warning('SIGTERM received...')
  # colorWipe(Color(0,0,0), 10)
  sio.disconnect()
  app.shutdown()
  app.cleanup()
  sys.exit(0)

signal.signal(signal.SIGINT, handler_stop_signals)
signal.signal(signal.SIGTERM, handler_stop_signals)

# sio.start_background_task(visualizer, CURRENT_COLOR)
web.run_app(app)

# if __name__ == '__main__':

#   try: 
#     # Initialize socketio server
#     # runner = web.AppRunner(app)
#     # thread1 = threading.Thread(target=socket_io_server, args=(runner, ))
#     # thread1.start()
    
#     # Initialize visualizer LEDs
#     # led_visualizer.update()
#     # thread2 = threading.Thread(target=visualizer, args=(CURRENT_COLOR, ))
#     # thread2.start()

#     web.run_app(app)


#   except KeyboardInterrupt:
#     logger.warning('Keyboard interrupt (SIGINT) received...')
#     colorWipe(Color(0,0,0), 10)
#     sys.exit(1)