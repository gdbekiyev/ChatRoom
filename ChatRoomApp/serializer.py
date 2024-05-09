from rest_framework import serializers

from ChatRoomApp.models import Message


class ChatApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
