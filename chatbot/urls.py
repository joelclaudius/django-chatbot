from django.urls import path
from . import views


#chatbot url
urlpatterns = [
    path('', views.chatbot, name='chatbot'),
]
