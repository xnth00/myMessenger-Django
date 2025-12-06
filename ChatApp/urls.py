from . import views
from django.urls import path

urlpatterns =[
    path('', include('ChatApp.urls')
    path('', views.CreateRoom, name='create-room'),
    path('<str:room_name>/<str:username>/', views.MessageView, name='room'),
]
