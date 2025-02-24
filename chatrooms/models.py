from django.db import models
from accounts.models import User

class Chatroom(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default="none")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "chatrooms"

class Message(models.Model):
    chatroom_id = models.ForeignKey(Chatroom, on_delete=models.CASCADE, related_name="messages")
    message_context = models.TextField()
    user_or_bot = models.BooleanField()
    reated_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "messages"