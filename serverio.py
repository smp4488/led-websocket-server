from led import set_color_hex, colorWipe
from aiohttp import web
import socketio

sio = socketio.AsyncServer(async_mode='aiohttp', cors_allowed_origins='*')
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
def set_color(sid, data):
    print('set_color ', data)
    set_color_hex(data)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

# app.router.add_routes(routes)
# app.router.add_static("/", rootdir)
# for resource in app.router.resources():
#   if resource.raw_match("/socket.io/"):
#     continue
#   cors.add(resource, { '*': aiohttp_cors.ResourceOptions(allow_credentials=True, expose_headers="*", allow_headers="*") })

if __name__ == '__main__':
    web.run_app(app)