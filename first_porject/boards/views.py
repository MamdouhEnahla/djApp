
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import addNewTopic
from .models import *

# homepage.
def home(request):
    boards = Board.objects.all()
    context ={
        'boards':boards
    }
    return render(request, 'home.html', context)

#view current topics
def getTopics(request, board_name):
    board = get_object_or_404(Board, name=board_name)
    context ={
        'board': board
    }
    
        
    return render(request, 'topics.html', context)

#add newTopic
@login_required
def addTopic(request, board_name):
    board = get_object_or_404(Board, name=board_name)
    user = request.user
    if request.method =='POST':
        form = addNewTopic(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.created_by = user
            topic.save()

            post= Post.objects.create(
                message = form.cleaned_data.get('message'),
                created_by = user,
                topic = topic,
            )
            return redirect('getTopics', board_name= board.name)
    else:
        form =addNewTopic()
    context={
                'board': board,
                'form': form,
            }
    return render(request, 'addtopic.html', context)

#about page
def about(request):
    return HttpResponse("<h1>About page</h1>")