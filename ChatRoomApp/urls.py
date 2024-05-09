from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from ChatRoomApp import views
from ChatRoomApp.consumer import ChatConsumer
from ChatRoomApp.views import SignInRoom, chatApi

urlpatterns = [
    path('login/', views.ChatLogin, name='ChatLogin'),
    path('', views.Chats, name='Chats'),
    path('SignInRoom/', SignInRoom, name="SignInRoom"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
    path('chatApi/', chatApi, name="chatApi"),
]
