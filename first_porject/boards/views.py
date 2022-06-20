from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import *
# homepage.

def home(request):
    boards = Board.objects.all()
    context ={
        'boards':boards
    }
    return render(request, 'home.html', context)

#view current topics
def getTopics(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    context ={
        'board': board
    }
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        user = User.objects.first()
        topic = Topic.objects.create(
            subject = subject,
            board = board_id,
            created_by = user,
            
        )
        post = Post.objects.create(
            message = message,
            topic = topic,
            created_by =user,
            
        )
        
    return render(request, 'topics.html', context)

#add newTopic
def addTopic(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    context={
        'board': board
    }
    return render(request, 'addtopic.html', context)

#about page
def about(request):
    return HttpResponse("<h1>About page</h1>")