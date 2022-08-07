
from .models import *
from django.db.models import Count
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import addNewTopic, PostForm
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# homepage.
class BoardListView(ListView):
    model = Board
    context_object_name = 'boards'
    template_name = 'home.html'

#view current topics
def board_topics(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    queryset  = board.topics.order_by('-created_at').annotate(comments =Count('posts'))
    page = request.GET.get('page', 1)
    paginator = Paginator(queryset, 18)
    try:
        topics = paginator.page(page)
    except PageNotAnInteger:
        topics = paginator.page(1)
    except EmptyPage:
        topics = paginator.page(paginator.num_pages)
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
    
    session_key = 'views_topic_{}'.format(topic.pk)
    if not request.session.get(session_key, False):
        topic.views += 1
        topic.save()
        request.session[session_key] = True
        
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
            topic.updated_by = request.user
            topic.updated_dt = timezone.now()
            topic.save()
            return redirect('topic_posts',board_id=board_id, topic_id = topic_id)
    else:
        form = PostForm()
    
    context={
        'topic':topic,
        'form': form, 
    }
    return render(request,'reply_topic.html', context)

#class-based-view
@method_decorator(login_required, name= "dispatch")
class PostUpdateView(UpdateView):
    model = Post
    fields = ("message",)
    template_name = 'edit_post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_dt = timezone.now()
        post.save()
        return redirect('topic_posts', board_id= post.topic.board.pk, topic_id= post.topic.pk )

#about page
def about(request):
    return HttpResponse("<h1>About page</h1>")