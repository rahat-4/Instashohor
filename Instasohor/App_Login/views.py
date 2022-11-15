from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from App_Login.models import Follow, UserProfile
from .forms import SignupForm, LoginForm, EditProfileForm
from App_Post.forms import PostForm
# Create your views here.

def sign_up(request):
    form = SignupForm()

    if request.method == "POST":
        form = SignupForm(data=request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("App_Login:log_in"))

    dict = {'title': "Signup", 'form':form}
    return render(request, "App_Login/sign_up.html", dict)

def log_in(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(data=request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")

        if form.is_valid():
            auth = authenticate(username=username, password=password)
            if auth:
                login(request, auth)
                return HttpResponseRedirect(reverse("App_Post:posts")) 
            else:
                return HttpResponse("Access deined!")

    dict = {'title': "Login", 'form':form}
    return render(request, "App_Login/log_in.html", dict)

@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse("App_Login:log_in"))

@login_required
def user_profile(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.user_post = request.user
            user.save()

            return HttpResponseRedirect(reverse("App_Post:posts"))
    dict = {'title': "Profile", 'form':form}
    return render(request, "App_Login/user_profile.html", dict)

@login_required
def edit_profile(request):
    current_user = UserProfile.objects.filter(new_user=request.user).first()
    form = EditProfileForm(instance=current_user)
    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=current_user)

        if form.is_valid():
            user = form.save(commit=False)
            user.new_user = request.user
            user.save()
            return HttpResponseRedirect(reverse("App_Login:user_profile"))
    dict = {'title': "Edit Profile", 'form': form}
    return render(request, "App_Login/edit_profile.html", dict)

@login_required
def other_user(request,pk):
    other_user = User.objects.get(pk=pk)
    follower_user = User.objects.get(username=request.user)
    followed = Follow.objects.filter(follower=other_user, following=follower_user)
    if followed:
        already_followed = True
    else:
        already_followed = False

    dict = {"other_user": other_user, "already_followed": already_followed}
    return render(request, "App_Login/other_user.html", dict)

@login_required
def follow_func(request,pk):
    following_user = User.objects.get(pk=pk)
    follower_user = User.objects.get(username=request.user)
    followed = Follow.objects.filter(follower=following_user,following=follower_user)
    if not followed:
        followed = Follow(follower=following_user,following=follower_user)
        followed.save()
    return HttpResponseRedirect(reverse("App_Login:other_user", kwargs={"pk":pk}))

@login_required
def unfollow_func(request,pk):
    following_user = User.objects.get(pk=pk)
    follower_user = User.objects.get(username=request.user)
    followed = Follow.objects.filter(follower=following_user,following=follower_user)
    if followed:
        followed.delete()
    return HttpResponseRedirect(reverse("App_Login:other_user", kwargs={"pk":pk}))