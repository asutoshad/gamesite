
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('', views.frontend, name='frontend'),
    path('homepage', views.fhome, name='fhome'),
    path('profile', views.profile, name='profile'),
    path('page/<str:pk_test>/', views.page, name='page'),
    path('register', views.registration, name='registration'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page='fhome'), name='logout'),

    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)