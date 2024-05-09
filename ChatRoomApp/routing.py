
from django.urls import path

from ChatRoomApp.consumer import ChatConsumer

websocket_urlpatterns = [
    path(r"chatws/", ChatConsumer.as_asgi())
]
