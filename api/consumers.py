import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from .models import message, chatRoom
from django.contrib.auth.models import User
from channels.db import database_sync_to_async

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    @database_sync_to_async
    def create_chat(self, user, room_name, message_data):
        User_model = User.objects.get(username=user)
        chatroom = chatRoom.objects.get(slug=room_name)
        message.objects.create(chatroom=chatroom, user=User_model, content=message_data)

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message_data = text_data_json["message"]
        room_name = text_data_json["room_name"]
        
        user = text_data_json["user"]
        # self.create_chat(user, room_name, message_data) 

        # Send message to room group
        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name, {"type": "chat.message", "message": message}
        # )
        async_to_sync(self.channel_layer.group_send)(
                    self.room_group_name, {"type": "chat.message", "message": message_data}  # Send the message ID instead of the whole object
                )
        self.create_chat(user, room_name, message_data)
    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))