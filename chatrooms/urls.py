from django.urls import path
from . import views


app_name = "chatrooms"


urlpatterns = [
    path("", views.Chatroom_List_APIView.as_view(), name="chatroom_list"),
    path("<int:pk>/", views.Chatroom_APIView.as_view(), name="chatroom"),
    path("<int:chatroom_pk>/messages/", views.Message_List_APIView.as_view(), name="message_list"),
    # path("<int:chatroom_pk>/user_message/", views.User_Message_APIView.as_view(), name="user_message"),
    # path("<int:chatroom_pk>/bot_message/", views.Bot_Message_APIView.as_view(), name="bot_message"),
]
