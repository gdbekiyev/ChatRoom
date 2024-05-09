from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json

from ChatRoomApp.models import Message


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        self.room_uuid = 'broad'
        self.group_name = 'castle'

        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        userID = text_data_json['userID']

        model = Message(sender=userID, content=message)

        model.save()

        async_to_sync(self.channel_layer.group_send)(self.group_name, {
            'type': 'chat_message',
            'userID': userID,
            'message': message

        })

    def chat_message(self, event):
        message = event['message']
        userID = event['userID']

        self.send(text_data=json.dumps({
            'message': message,
            'userID': userID,

        }))
