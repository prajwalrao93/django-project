from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import RegisterUser, PostForm, ProfileForm, CommentForm, MessageForm
from django.contrib import messages
from .models import Posts, Profile, Comment, Message

# Create your views here.
def home(request):
    form = PostForm(request.POST or None, request.FILES)
    posts = Posts.objects.all().order_by("-created_at")
    if request.method == "POST":
        for ind_post in posts:
            cmnt_post = get_object_or_404(Posts, id=ind_post.id)
            comment_form = CommentForm(request.POST, instance=cmnt_post)
            if comment_form.is_valid():
                if request.POST['upload'] == 0:
                    Comment.objects.create(body=request.POST["body"], post=Posts.objects.get(id=request.POST['upload']),
                                           user_id=request.user)
                    return redirect('home')
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, ("Post Successful"))
            return redirect('home')
    form = PostForm()
    comment_form = CommentForm()
    return render(request, "home.html", {"posts": posts, "form": form, "comment_form": comment_form})

def register_user(request):
    form = RegisterUser()
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect('home')
    return render(request, 'register.html', {"form":form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Login Successful!"))
            return redirect('home')
        else:
            messages.success(request, ("Check Login details"))
            return redirect('home')
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    messages.success(request, "You have been Logged Out.")
    return redirect('home')

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        posts = Posts.objects.filter(user_id=pk).order_by('-created_at')
        profile1 = request.user.profile
        form = ProfileForm(request.POST, request.FILES, instance=profile1)
        if request.method == "POST":
            for ind_post in posts:
                cmnt_post = get_object_or_404(Posts, id=ind_post.id)
                comment_form = CommentForm(request.POST, instance=cmnt_post)
                if comment_form.is_valid():
                    Comment.objects.create(body=request.POST["body"], post=Posts.objects.get(id=request.POST['upload']),
                                           user_id=request.user)
                    comment_form = CommentForm()
                    return render(request, 'profile.html', {"profile": profile, "posts": posts, "form": form,
                                                            "comment_form":comment_form})
            if form.is_valid():
                form.save()
                post = form.save(commit=False)
                post.user = request.user
                messages.success(request, ("Post Successful"))
                profile = Profile.objects.get(user_id=pk)
                comment_form = CommentForm()
                return render(request,'profile.html', {"profile":profile, "posts":posts, "form": form,
                                                       "comment_form":comment_form})
        form = ProfileForm(instance=profile1)
        comment_form = CommentForm()
        return render(request,'profile.html', {"profile":profile, "posts":posts, "form": form,
                                               "comment_form":comment_form})
    else:
        messages.success(request, ("You must be Logged In to view this page"))
        return redirect('home')

def edit_post(request, pk):
    post = get_object_or_404(Posts, id=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            post1 = form.save(commit=False)
            post1.user = request.user
            post1.save()
            messages.success(request, ("Successfully saved"))
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {"form":form})


def delete_post(request, pk):
    post = get_object_or_404(Posts, id=pk)
    post.delete()
    messages.success(request, ("Post Deleted Successfully!"))
    return redirect('home')

def like_post_profile(request, pk):
    post = get_object_or_404(Posts, id=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    if post.number_of_likes() == 1:
        post.like_status = False
    else:
        post.like_status = True
    post.save()
    profile = Profile.objects.get(user=post.user)
    pk = profile.user.id
    return redirect(reverse('profile', args=[str(pk)]))

def like_post_home(request, pk):
    post = get_object_or_404(Posts, id=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    if post.number_of_likes() == 1:
        post.like_status = False
    else:
        post.like_status = True
    post.save()
    return redirect('home')

def profile_list(request):
    profiles = Profile.objects.exclude(user_id = request.user.id)
    if request.method == 'POST':
        profile = Profile.objects.get(user_id=request.POST['follow'].split(" ")[1])
        current_profile =  Profile.objects.get(user_id=request.user.id)
        if 'unfollow' in request.POST['follow']:
            current_profile.follows.remove(profile)
        elif 'follow' in request.POST['follow']:
            current_profile.follows.add(profile)
    return render(request, 'profile_list.html', {'profiles': profiles})


def message_link(request, pk):
    profile = Profile.objects.get(user_id=pk)
    message_list = Message.objects.filter(Q(sent_by=request.user) | Q(user=request.user)).order_by('sent_on')
    message_list = message_list.distinct()
    form = MessageForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            message_rcvd = form.save(commit=False)
            message_rcvd.sent_by = request.user
            message_rcvd.user = profile.user
            message_rcvd.save()
            return redirect(reverse('message_link', args=[str(pk)]))
    form = MessageForm()
    return render(request, 'message_link.html', {'message_list':message_list, 'profile':profile, 'form':form})
