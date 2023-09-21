from django.urls import path
from .views import RegisterView, LoginView, LogoutView, SuggestedFriendsView, PingView, OnlineUsersView, StartChatView, index, room, login, register

urlpatterns = [
    path("loginpage/", login, name="login"),
    path ("registerpage/", register, name="register"),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('suggested-friends/<int:user_id>', SuggestedFriendsView.as_view()),
    path('online-users/', OnlineUsersView.as_view()),
    path('chat/start/', StartChatView.as_view(), name='start_chat'),
    path("", index, name="index"),
    path("<str:room_name>/", room, name="room"),

]
