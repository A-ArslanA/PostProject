from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import AddPostForm

def homePage(request):
    posts = Post.objects.all().order_by('-postDate')[:3]
    return render(request, "news/home.html", {
        'posts': posts
    })

def allPost(request):
    posts = Post.objects.all().order_by('-postDate')
    return render(request, "news/all-news.html", {
        'posts': posts
    })

def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "user/post-detail.html", {
        'post': post
    })

def addPost(request):
    if request.method == "POST":
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homePage")
    else:
        form = AddPostForm()

    return render(request, "user/add-post.html", {
        'form': form
    })

def deletePost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("allPost")
    return render(request, "user/delete-post.html", {
        'post': post
    })

def editPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = AddPostForm(request.POST or None, instance=post)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("postDetail", pk=post.pk)
    else:
        form = AddPostForm()

    return render(request, "user/edit-post.html", {
        'post': post,
        'form': form
    })





