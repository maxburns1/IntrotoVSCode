from django.http import Http404
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')

@login_required
def topics(request):
    topic = Topic.objects.filter(owner=request.user).order_by('date_added')
    
    context = {'all_topics': topic}

    return render(request, 'mainapp/topics.html', context)

@login_required
def topic(request, topic_id):
    t = Topic.objects.get(id=topic_id)
    entries = Entry.objects.filter(topic=t).order_by('-date_added')

    if t.owner != request.user:
        raise Http404

    context = {'topic':t, 'entries':entries}

    return render(request, 'mainapp/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
       
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()

            return redirect('mainapp:topics')

    context = {'form': form}
    
    return render(request, 'mainapp/new_topic.html', context)
@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    
    if topic.owner != request.user:
        raise Http404


    if request.method != 'POST':
        
        form = EntryForm()
    else:
        
        form = EntryForm(data=request.POST)
        if form.is_valid():
            
            new_entry = form.save(commit=False)
            
            new_entry.topic = topic
            
            new_entry.save()
           
            return redirect('mainapp:topic', topic_id=topic_id)

  
    context = {'topic': topic, 'form': form}
    return render(request, 'mainapp/new_entry.html', context)
@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(data=request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('mainapp:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'mainapp/edit_entry.html', context)