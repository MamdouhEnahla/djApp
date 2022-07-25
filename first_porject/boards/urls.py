from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('about/', views.about, name='about'),
    path('boards/<int:board_id>', views.getTopics, name="getTopics"),
    path('boards/<int:board_id>/new', views.addTopic, name="addTopic"),
    path('boards/<int:board_id>/topics/<int:topic_id>', views.topic_posts, name="topic_posts"),

]