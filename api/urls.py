from django.urls import path
from .views import RegisterView, LoginView, LogoutView, SuggestedFriendsView, OnlineUsersView, StartChatView, index, room, login, register

urlpatterns = [
    path("login/", login, name="login"),
    path ("register/", register, name="register"),
    path('registerapi/', RegisterView.as_view()),
    path('loginapi/', LoginView.as_view()),
    path('logoutapi/', LogoutView.as_view()),
    path('suggested-friends/<int:user_id>', SuggestedFriendsView.as_view()),
    path('online-users/', OnlineUsersView.as_view()),
    path('chat/start/', StartChatView.as_view(), name='start_chat'),
    path("", index, name="index"),
    path("<str:room_name>/", room, name="room"),

]
