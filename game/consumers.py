import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.generic.websocket import WebsocketConsumer
from random import randint
from time import sleep



#*********** question here I should define game status and echos it whenever it changed ********
class GameStatusConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        gameStatus = text_data_json['gameStatus']

        self.send(text_data=json.dumps({
            'gameStatus': gameStatus
        }))











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