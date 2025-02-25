from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.core import serializers

# from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

# import os
# import sys
# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from .models import Chatroom, Message
from .serializers import ChatRoomSerializer
from .serializers import MessageSerializer

from LangChain.main_chatbot import chatbot

class Chatroom_List_APIView(APIView):
    def get(self, request):
        chatrooms = Chatroom.objects.all()
        serializer = ChatRoomSerializer(chatrooms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        # print(request.user.id)
        request.data["user_id"] = request.user.id
        serializer = ChatRoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

class Chatroom_APIView(APIView):
    def get(self, request, pk):
        chatroom = get_object_or_404(Chatroom, pk=pk)
        serializer = ChatRoomSerializer(chatroom)
        return Response(serializer.data)
        
    def delete(self, request, pk):
        chatroom = get_object_or_404(Chatroom, pk=pk)
        chatroom.delete()
        return Response(status=204)
        
class Message_List_APIView(APIView):
    def get(self, request, chatroom_pk):
        chatroom = get_object_or_404(Chatroom, pk=chatroom_pk)
        messages = chatroom.messages.all()
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
    
    def post(self, request, chatroom_pk):
        # print(chatroom_pk)
        request.data["chatroom_id"] = chatroom_pk
        request.data["user_or_bot"] = 1
        serializer = MessageSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
        else: Response(serializer.errors, status=400)
        
        request.data["user_or_bot"] = 0
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        # print("message_context :", request.data["message_context"])
        
        request.data["message_context"] = chatbot(request.data["message_context"])
        # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        # print("message_context :", request.data["message_context"])
        
        serializer = MessageSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: Response(serializer.errors, status=400)


# class User_Message_APIView(APIView):
    

# class Bot_Message_APIView(APIView):
#     def post(self, request, chatroom_pk):
#         # print("test")
#         request.data["user_or_bot"] = 0
#         request.data["chatroom_id"] = chatroom_pk
#         # print(request.data["message_context"])
#         # print(chatbot(request.data["message_context"]))
#         request.data["message_context"] = chatbot(request.data["message_context"])
#         print(request.data)
#         serializer = MessageSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)