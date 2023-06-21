from django.db import models

class Message(models.Model):
    PARTICIPANT_CHOICES = [
        ('AI', 'AI'),
        ('Human', 'Human'),
    ]

    participant = models.CharField(max_length=10, choices=PARTICIPANT_CHOICES)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

