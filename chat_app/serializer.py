from rest_framework import serializers
from chat_app.models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['participant', 'text', 'timestamp']