from django.db.models import Count
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import addNewTopic, PostForm
from .models import *

# homepage.
def home(request):
    boards = Board.objects.all()
    context ={
        'boards':boards
    }
    return render(request, 'home.html', context)

#view current topics
def board_topics(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    topics  = board.topics.order_by('-created_at').annotate(comments =Count('posts'))
    context ={
        'board': board,
        'topics': topics,
    }
    
    return render(request, 'board_topics.html', context)

#add newTopic
@login_required
def new_topic(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
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
            return redirect('board_topics', board_id= board.pk)
    else:
        form =addNewTopic()
    context={
                'board': board,
                'form': form,
            }
    return render(request, 'new_topic.html', context)

#get topic posts
def topic_posts(request, board_id, topic_id):
    topic = get_object_or_404(Topic, board__pk= board_id, pk= topic_id)
    context ={
        'topic':topic
    }
    return render(request, 'topic_posts.html', context)

#reply_topic
@login_required
def reply_topic(request, board_id,topic_id):
    topic = get_object_or_404(Topic,board__pk=board_id,pk=topic_id)
    if request.method == "POST":
        form =PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()

            return redirect('topic_posts',board_id=board_id, topic_id = topic_id)
    else:
        form = PostForm()
    
    context={
        'topic':topic,
        'form': form, 
    }
    return render(request,'reply_topic.html', context)

#about page
def about(request):
    return HttpResponse("<h1>About page</h1>")