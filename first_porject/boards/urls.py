from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('boards/<str:board_name>', views.getTopics, name="getTopics"),
    path('boards/<str:board_name>/new', views.addTopic, name="addTopic"),
]