from django.shortcuts import render, redirect, get_object_or_404
from admindashboard.models import Gamedb 
 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def frontend(request):
    return render(request,'findex.html')



def fhome(request):
    all_items = Gamedb.objects.all()  # Retrieve all items from the Gamedb model
    top_posts = Gamedb.objects.order_by('-views')[:1]
    top_four = Gamedb.objects.order_by('-views')[1:5]
    latest = Gamedb.objects.order_by('-release_date')[:5]
    return render(request, 'homepage.html', {'all_items': all_items, 'top_posts': top_posts,'top_four': top_four,'latest': latest})

@login_required
def profile(request):
    return render(request, 'registration/userprofile.html')


def page(request, pk_test):
    posts = get_object_or_404(Gamedb, pk=pk_test)
    posts.views += 1
    posts.save()
    post = Gamedb.objects.get(id=pk_test)
    all_items = Gamedb.objects.all()
    top_posts = Gamedb.objects.order_by('-views')[:1]
    top_four = Gamedb.objects.order_by('-views')[1:5]
    latest = Gamedb.objects.order_by('-release_date')[:5]
    return render(request, 'page.html', {'post': post, 'all_items': all_items,'posts': posts,'top_posts': top_posts,'top_four': top_four,'latest': latest})


def registration(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = UserCreationForm()
    return render (request,'registration/register.html',{'form':form})








