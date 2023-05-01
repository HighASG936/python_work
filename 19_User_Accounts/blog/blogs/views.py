from django.shortcuts import render, redirect
from .models import BlogPost, Entry
from .forms import BlogForm

def index(request):
    """Home page"""
    return render (request, 'blogs/index.html')

def posts(request):
    """Show all posts"""
    posts = BlogPost.objects.order_by('date_added')
    context = {'posts' : posts }
    return render (request, 'blogs/posts.html', context)

def post(request, post_id):
    """Show single post and its content"""
    post = BlogPost.objects.get(id=post_id)
    entries = post.entry_set.order_by('-id')
    context = {'post': post, 'entries': entries}
    return render (request, 'blogs/post.html', context)

def new_post(request):
    """Enter new post"""
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = BlogForm()
    else:
        #POST data submitted; process data.
        form = BlogForm(data=request.POST)    
        if form.is_valid():
            form.save()
            return redirect ('blogs:posts')
    #Display a blank or invalid form
    context = {'form': form}
    return render (request, 'blogs/new_post.html', context)

def new_entry(request, entry_id):
    """Enter new entry"""
    entry = BlogPost.objects.get(id=entry_id)
    if request.method != 'POST':
        #No data submitted; create a blank form.
        form = BlogForm()
    else:
        #POST data submitted; process data.
        form = BlogForm(data=request.POST)  
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.entry = entry
            new_entry.save()
            return redirect ('blogs:post', post_id=entry_id)
    #Display a blank or invalid form
    context = {'entry': entry, 'form': form}
    return render (request, 'blogs/new_entry.html', context)

def edit_post(request, entry_id):
    """Edit existing post"""
    entry = Entry.objects.get(id=entry_id)
    title = entry.title

    if request.method != 'POST':
        #Initial request; pre-fill with the current entry.
        form = BlogForm(instance=entry)
    else:
        #POST data submitted; process data.
        form = BlogForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:post', post_id=entry.id)

    context = {'entry':entry, 'title': title, 'form': form}
    return render(request, 'blogs/edit_post.html', context)


