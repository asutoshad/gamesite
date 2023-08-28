
from django.urls import path
from . import views

urlpatterns = [
    path('adminhome', views.adminhome, name='adminhome'),
    path('postform',views.postform,name='postform'),

]
