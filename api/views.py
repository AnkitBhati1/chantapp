from django.shortcuts import render
from rest_framework.views import APIView
from api.helpers import get_top_friends
from .serializers import UserSerializer, StartChatSerializer
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework import status
import json
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from datetime import datetime , timedelta
from django.db.models import Q
from django.contrib.auth.models import User
from .models import chatRoom

# Create your views here.
with open('users.json') as f:
    users_data = json.load(f)['users']

# Register View

def index(request):
    now = datetime.now()
    expire_minutes = 60
    tokens = Token.objects.filter(Q(created__gte=now - timedelta(minutes=expire_minutes)) | Q(user__isnull=True))
    online_users = []
    for token in tokens:
        online_users.append(token.user.username)
    
    context = {
        "online_users": online_users
    }
    
    return render(request, "api/index.html" , context)


def room(request, room_name):
    return render(request, "api/room.html", {"room_name": room_name})

def login(request):
    return render(request, "api/login.html", {})

def register(request):
    return render(request, "api/register.html", {})

class RegisterView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

# Login View


class LoginView(APIView):
    serializer_class = UserSerializer

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            # Implement token or session-based authentication here
            expire_minutes = 60
            now = datetime.now()
            expired_tokens = Token.objects.filter(user=user)
            expired_tokens.delete()
            token = Token.objects.create(user=user)
            return Response({"message": "Login successful", "user": username, "token": token.key}, status=status.HTTP_200_OK)
        return Response({"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)

# Logout View


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        # Implement token or session-based authentication here
        #delete token
        request.user.auth_token.delete()
        return Response({"message": "Logout successful"}, status=status.HTTP_200_OK)

# Suggested Friends View


class SuggestedFriendsView(APIView):
    def get(self, request, user_id):
        top_friends = get_top_friends(users_data, user_id, top_n=5)
        return Response({"message": "Top friends retrieved successfully", "top_friends": top_friends}, status=status.HTTP_200_OK)
    

# Online Users View

class OnlineUsersView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        # Implement token or session-based authentication here
        #get all users with token
        now = datetime.now()
        expire_minutes = 60
        tokens = Token.objects.filter(Q(created__gte=now - timedelta(minutes=expire_minutes)) | Q(user__isnull=True))
        online_users = []
        for token in tokens:
            online_users.append(token.user.username)
        return Response({"message": "Online users retrieved successfully", "online_users": online_users}, status=status.HTTP_200_OK)

# Start Chat View

class StartChatView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = StartChatSerializer
    def post(self, request):
        # Implement token or session-based authentication here
        #get all users with token
        serializer = StartChatSerializer(data=request.data)
        now = datetime.now()
        expire_minutes = 60
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=serializer.data.get("username"))
        # print(user.auth_token)
        tokens = Token.objects.filter(Q(created__gte=now - timedelta(minutes=expire_minutes)), user=user)
        print(tokens)
        if not tokens:
            return Response({"message": "error"}, status=status.HTTP_401_UNAUTHORIZED)
        
        user_ids = [user.id, request.user.id]
        user_ids.sort()
        room_name = f"{user_ids[0]}_{user_ids[1]}"
        try:
            chatRoom.objects.get(name=room_name)
        except chatRoom.DoesNotExist:
            chatroom = chatRoom()
            chatroom.name = room_name
            chatroom.slug = room_name
            chatroom.save()
            chatroom.user.add(user, request.user)
            chatroom.save()
        return Response({"message": "Chat started successfully", "room_name": room_name}, status=status.HTTP_200_OK)
