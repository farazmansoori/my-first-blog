from django.shortcuts import render

from django.utils import timezone

from .models import Post # Importing Post Model form medels.py. (.) Dot before models means current directory/application. This means we can use . and the name of the file (without .py).

# Create your views here.

'''
def post_list(request):
    return render(request, 'blog/post_list.html', {})
'''
def post_list(request):
    # posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})