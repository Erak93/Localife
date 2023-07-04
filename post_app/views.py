from django.shortcuts import render
from .models import Post

# Create your views here.

# def post_app(request):
#     return render(request,'post_app/post_app.html')

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_app/post_list.html', {'posts': posts})

def post_create(request):
    return render(request, 'post_app/post_create.html')

def post_detail(request, pk):
    return render(request, 'post_app/post_detail.html')

def post_update(request, pk):
    return render(request, 'post_app/post_update.html')

def post_delete(request, pk):
    return render(request, 'post_app/post_delete.html')

def post_like(request, pk):
    return render(request, 'post_app/post_like.html')

def post_unlike(request, pk):
    return render(request, 'post_app/post_unlike.html')

