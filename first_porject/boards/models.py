from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Board(models.Model):
    name  = models.CharField(max_length=50, unique=True)
    desc = models.CharField(max_length=150, )
    
    def __str__(self) -> str:
        return self.name

class Topic(models.Model):
    subject = models.CharField(max_length=255)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='topics', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # def __str__(self) -> str:
    #     return self.subject

class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self) -> str:
    #     return self.message
