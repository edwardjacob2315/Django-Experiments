from django.contrib import admin

from .models import Post
from .models import Robot
from .models import Pilot

admin.site.register(Post)
admin.site.register(Pilot)
admin.site.register(Robot)
