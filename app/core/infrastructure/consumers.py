from channels.generic.websocket import AsyncWebsocketConsumer
from django.conf import settings
import json
import asyncio
import websockets


class TradeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("WebSocket connected")
        ws_btcusdt = settings.WS_BTCUSDT
        asyncio.create_task(self.consume_stream(ws_btcusdt))

    async def disconnect(self, close_code):
        pass

    async def consume_stream(self, stream_url):
        async with websockets.connect(stream_url) as ws:
            while True:
                data = await ws.recv()
                data_json = json.loads(data)
                #print("Received data: ", data_json)
                await self.send(text_data=json.dumps({
                    'type': 'bookTicker',
                    'data': data_json
                }))

    async def receive(self, text_data=None, bytes_data=None):
        pass
