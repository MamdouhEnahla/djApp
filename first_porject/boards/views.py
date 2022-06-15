
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Board
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