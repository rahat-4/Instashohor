from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User

from App_Login.models import Follow
from .models import Post, Like
# Create your views here.

@login_required
def posts(request):
    user = User.objects.get(username=request.user)
    following_list = Follow.objects.filter(following=user)
    all_post = Post.objects.filter(user_post__in=following_list.values_list("follower"))
    post = Like.objects.filter(liker=user)
    like_post_list = post.values_list('liked_post', flat=True)

    if request.method == "GET":
        search = request.GET.get('search','')
        search_users = User.objects.filter(username__icontains=search)
    dict = {'title':"Posts", "like_post_list": like_post_list ,"all_post": all_post, 'search':search, 'search_users': search_users}
    return render(request, "App_Post/posts.html", dict)

@login_required
def create_post(request):
    dict = {'title': "New Post"}
    return render(request, "App_Post/create_post.html", dict)

@login_required
def liked(request,pk):
    liker = User.objects.get(username=request.user)
    liked_post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(liker=liker, liked_post=liked_post)
    if not already_liked:
        already_liked = Like(liker=liker, liked_post=liked_post)
        already_liked.save()
    return HttpResponseRedirect(reverse("App_Post:posts"))

@login_required
def unliked(request,pk):
    liker = User.objects.get(username=request.user)
    liked_post = Post.objects.get(pk=pk)
    already_liked = Like.objects.filter(liker=liker, liked_post=liked_post)
    if already_liked:
        already_liked.delete()
    return HttpResponseRedirect(reverse("App_Post:posts"))