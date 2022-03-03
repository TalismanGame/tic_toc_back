import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer
from random import randint
from time import sleep
from asgiref.sync import async_to_sync
from .models import Game
from asgiref.sync import sync_to_async


#*********** question here I should define game status and echos it whenever it changed ********
class GameStatusConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]

        #comment this after all done and set for authentication purposes
        await self.accept()

        #uncomment this after all done and set for authentication purposes
        # if self.user.is_authenticated:
        #     await self.accept()
        #     # group_name = f"targetGame{targetGame}"
        #     # self.groups.append(group_name)

        #     # await self.channel_layer.group_add(
        #     #     group_name,
        #     #     self.channel_name,
        #     # )
        # else:
        #     await self.close()

    async def receive_json(self, content, **kwargs):
        code = content["code"]
        self.group_name = code

        try:
            targetGame = await sync_to_async(Game.objects.get, thread_sensitive=True)(inviteCode=code)
            await self.send_json({"status is": targetGame.status})
        except: 
            await self.send_json({"error": "game not found"})
            await self.close()

    async def disconnect(self, close_code):
        pass
    
    async def echo(self, event):
        await self.send_json(event["content"])