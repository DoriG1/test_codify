# test_codify
Тестовое задание для CODIFY на позицию Junior Python веб-разработчика
Цель: Разработать небольшой Django Rest Framework проект - чат с GPT используя OpenAI API.

Данный проект разработан на Django Rest Framework, который включать модель для сообщений, содержащая тип участника переписки (AI/Human), 
текст сообщения и временную метку.

POST запрос должен позволять пользователю отправлять сообщение в чат. Отправленное сообщение следует передать модели GPT используя OpenAI API, 
получить от неё ответ, а затем сохранить оба сообщения в базе данных.

GET запрос должен позволять получать историю переписки.

API ключ не включен в код приложения.



В данной проекте возникли проблемы с API ключом, возможно срок его действия уже завершился и не получается получить ответ от AI.
При тестировании в Postman:
         POST запрос:          http://127.0.0.1:8000/api/send-message/
1) Во вкладке headers прописать свой Content-Type : application/json
2) В body>raw прописать запрос в json формате: 
{
  "participant": "Human",
  "text": "Hello, how are you?"
}

       
        GET запроc:            http://localhost:8000/api/chat-history/