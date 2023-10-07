from django.shortcuts import render, redirect, get_object_or_404
from admindashboard.models import Gamedb, Comment
 
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



from admindashboard.forms import CommentForm

def page(request, pk_test):
    posts = get_object_or_404(Gamedb, pk=pk_test)
    posts.views += 1
    posts.save()
    post = Gamedb.objects.get(id=pk_test)
    all_items = Gamedb.objects.all()
    top_posts = Gamedb.objects.order_by('-views')[:1]
    top_four = Gamedb.objects.order_by('-views')[1:5]
    latest = Gamedb.objects.order_by('-release_date')[:5]




    gamedb = get_object_or_404(Gamedb, pk=pk_test)

    if request.method == 'POST':
        message = request.POST.get('message')
        user = request.user  # Get the currently logged-in user

        # Create a Comment object and set user and gamedb fields
        comment = Comment(user=user, gamedb=gamedb, message=message)
        comment.save()

        return redirect('page', pk_test=pk_test)
    else:
        comment_form = CommentForm()

    # Fetch other data as needed
    all_items = Gamedb.objects.all()
    top_posts = Gamedb.objects.order_by('-views')[:1]
    top_four = Gamedb.objects.order_by('-views')[1:5]
    latest = Gamedb.objects.order_by('-release_date')[:5]


    comments = Comment.objects.filter(gamedb=gamedb)

    return render(request, 'page.html', {
        'post': gamedb,
        'all_items': all_items,
        'top_posts': top_posts,
        'top_four': top_four,
        'latest': latest,
        'comment_form': comment_form,
        'comments': comments,  
    })


    # return render(request, 'page.html', {'post': post, 'all_items': all_items,'posts': posts,'top_posts': top_posts,'top_four': top_four,'latest': latest})


def registration(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = UserCreationForm()
    return render (request,'registration/register.html',{'form':form})






# @login_required
# def add_comment_to_gamedb(request, gamedb_id):
#     gamedb = get_object_or_404(Gamedb, pk=gamedb_id)

#     if request.method == 'POST':
#         message = request.POST.get('message')
#         user = request.user  # Get the currently logged-in user

#         comment = Comment(user=user, gamedb=gamedb, message=message)
#         comment.save()

#         # Redirect to the gamedb detail page or wherever you want
#         return redirect('gamedb_detail', gamedb_id=gamedb_id)

#     # Handle the GET request (e.g., render a form for adding comments)
#     return render(request, 'page.html', {'gamedb': gamedb})


