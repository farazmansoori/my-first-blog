# from django.contrib import admin

from django.contrib import admin
from .models import Post # To make our model visible on the admin page, we need to register the model

admin.site.register(Post)