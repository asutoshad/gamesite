from django.contrib import admin

# Register your models here.

from .models import Gamedb
from .models import BlogPost



# Register your models here.

admin.site.register(Gamedb)
admin.site.register(BlogPost)


