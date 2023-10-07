
from django.urls import path
from . import views


urlpatterns = [
    path('adminhome', views.adminhome, name='adminhome'),
    path('postform',views.postform,name='postform'),
    path('postdetail/<int:pk>/', views.blog_post_detail, name='blog_post_detail'),
    

]
