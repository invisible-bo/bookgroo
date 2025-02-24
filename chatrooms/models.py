from django.db import models
from accounts.models import User


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Chatroom(TimeStampModel):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default="none")

    class Meta:
        db_table = "chatrooms"


class Message(TimeStampModel):
    chatroom_id = models.ForeignKey(
        Chatroom, on_delete=models.CASCADE, related_name="messages"
    )
    message_context = models.TextField()
    user_or_bot = models.BooleanField()

    class Meta:
        db_table = "messages"
