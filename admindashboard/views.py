from django.shortcuts import render, redirect, get_object_or_404
from .models import Gamedb
from .forms import GameForm
from .models import BlogPost


from django.contrib import messages

# Create your views here.

def adminhome(request):
    return render(request, 'index.html')

def postform(request):
    if request.method == 'POST':
        fm = GameForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if fm.is_valid():
            fm.save()
            fm.save_m2m()
            messages.success(request, 'New item added.')
        else:
            messages.error(request, 'Invalid form data.')
    else:
        fm = GameForm()

    all_items = Gamedb.objects.all()
    return render(request, 'posts/create.html', {'form': fm, 'all_items': all_items})

def blog_post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    
    # Increment the view count for this blog post
    post.views += 1
    post.save()
    
    return render(request, 'posts/post_detail.html', {'post': post})