import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from chat_app.serializer import MessageSerializer
from key import API_KEY
from rest_framework import status

API_KEY = 'YOUR_API_KEY'  # Замените на ваш ключ API

@api_view(['POST'])
def send_message(request):
    serializer = MessageSerializer(data=request.data)
    if serializer.is_valid():
        message_text = serializer.validated_data['text']
        message = serializer.save(participant='Human')
        
        # Отправка запроса к OpenAI API
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers={
                'Authorization': f'Bearer {API_KEY}',
                'Content-Type': 'application/json',
            },
            json={
                'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'},
                             {'role': 'user', 'content': message_text}],
            }
        )
        
        # Получение ответа от OpenAI API
        if response.status_code == 200:
            data = response.json()
            reply = data['choices'][0]['message']['content']
            
            # Сохранение сообщений в базе данных
            ai_message = Message.objects.create(participant='AI', text=reply)
            ai_serializer = MessageSerializer(ai_message)
            return Response(ai_serializer.data)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_chat_history(request):
    messages = Message.objects.all().order_by('timestamp')
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data)
