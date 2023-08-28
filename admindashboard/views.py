from django.shortcuts import render, redirect
from .models import Gamedb
from .forms import GameForm

from django.contrib import messages

# Create your views here.

def adminhome(request):
    return render(request, 'index.html')

def postform(request):
    if request.method == 'POST':
        form = GameForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = Gamedb.objects.all()
            messages.success(request,('new item added......'))
            return render (request, 'posts/create.html' , {'all_items':all_items})
        
        else:
            messages.error(request, 'Invalid form data. Please check your inputs.')
            return redirect('postform')
        


    else:
        all_items = Gamedb.objects.all()
        return render (request, 'posts/create.html' , {'all_items':all_items})
    

