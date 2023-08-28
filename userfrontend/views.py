from django.shortcuts import render
from admindashboard.models import Gamedb 

# Create your views here.
def frontend(request):
    return render(request,'findex.html')

def fhome(request):
    all_items = Gamedb.objects.all()  # Retrieve all items from the Gamedb model
    return render(request, 'homepage.html', {'all_items': all_items})
