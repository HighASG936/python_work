from django.shortcuts import render, redirect
from .models import BlogPost, BlogEntry
from .forms import BlogForm, EntryForm

def index(request):
    return render(request, 'blogs/index.html')

def posts(request):
    posts = BlogPost.objects.order_by('data_added')
    context = {'posts': posts}
    return render(request, 'blogs/posts.html', context)

def post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    entries = post.blogentry_set.order_by('-date_added')
    context = {'post': post, 'entries': entries}
    return render(request, 'blogs/post.html', context)

def new_post(request):
    if request.method != 'POST':
        #No data submmited; create a blank form
        form = BlogForm()
    else:
        #POST data submitted; process data
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:posts')

    #Display a blank or invalid form
    context ={'form': form }
    return render(request, 'blogs/new_post.html', context)

def new_entry(request, post_id):
    post = BlogPost.objects.get(id=post_id)

    if request.method != 'POST':
        #No data submitted; create a blank form
        form = EntryForm()
    else:
        #POST data submitted; process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.post = post
            new_entry.save()
            return redirect('blogs:post', post_id=post_id)
    #Display a blank or invalid form
    context = {'post': post, 'form': form}
    return render(request, 'blogs/new_entry.html', context)

def edit_entry(request, entry_id):
    entry = BlogEntry.objects.get(id=entry_id)
    post = entry.post

    if request.method != 'POST':
        #Initial request; pre-fill form with the current entry
        form = EntryForm(instance=entry)
    else:
        #POST data submitted; process data
        form = BlogForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=post.id)

    context = {'entry': entry, 'post': post, 'form': form}
    return render(request, 'blogs/edit_entry.html', context)





