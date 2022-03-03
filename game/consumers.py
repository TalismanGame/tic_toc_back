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
# class GameStatusConsumer(AsyncJsonWebsocketConsumer):
#     async def connect(self):
#         await self.accept()

#         # async def test_can_send_and_receive_messages(self, settings):
#         #     settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
#         #     communicator = WebsocketCommunicator(
#         #         application=application,
#         #         path='/taxi/'
#         #     )
#         #     await communicator.connect()
#         #     message = {
#         #         'type': 'echo.message',
#         #         'data': 'This is a test message.',
#         #     }
#         #     await communicator.send_json_to(message)
#         #     response = await communicator.receive_json_from()
#         #     assert response == message
#         #     await communicator.disconnect()

#     async def disconnect(self, code):
#         await super().disconnect(code)

class GameStatusConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.user = self.scope["user"]
        # self.code = self.scope["code"]
        if self.user.is_authenticated:
            await self.accept()
            # group_name = f"portfolios_{portfolio_id}"
            # self.groups.append(group_name)

            # await self.channel_layer.group_add(
            #     group_name,
            #     self.channel_name,
            # )
        else:
            await self.close()

    async def receive_json(self, content, **kwargs):
        code = content["code"]

        try:
            targetGame = await sync_to_async(Game.objects.get, thread_sensitive=True)(inviteCode=code)
            await self.send_json(
                            {
                                "status is": targetGame.status
                            }
                        )
        except: 
            await self.send_json(
                {
                    "error": "game not found"
                }
            )
            await self.close()


    async def echo(self, event):
        await self.send_json(event["content"])

    async def disconnect(self, close_code):
        pass


# class PracticeConsumer(AsyncConsumer):

#     async def websocket_connect(self,event):
#         # when websocket connects
#         print("connected",event)

#         await self.send({"type": "websocket.accept",
#                          })



#         await self.send({"type":"websocket.send",
#                          "text":0})





#     async def websocket_receive(self,event):
#         # when messages is received from websocket
#         print("receive",event)



#         sleep(1)

#         await self.send({"type": "websocket.send",
#                          "text":str(randint(0,100))})




#     async def websocket_disconnect(self, event):
#         # when websocket disconnects
#         print("disconnected", event)