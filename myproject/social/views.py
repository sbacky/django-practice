# social/views.py

from django.shortcuts import render, redirect

from .models import Profile, Messages
from .forms import MessageForm


def dashboard(request):
    if not request.user.is_authenticated:
       return redirect('users:login')
    # Get form from request
    form = MessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('social:dashboard')
    # Get all posts from followers and order by -created_at
    followed_messages = Messages.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")    
    
    return render(
        request,
        "social/dashboard.html",
        {"form": form, "messages": followed_messages},
    )


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "social/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    # Create profile for any user that doesnt have one
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()
    # Update followers for profile at pk in request URL
    profile = Profile.objects.get(pk=pk)
    if request.method =="POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == 'unfollow':
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    # Get follower, following, and message count
    follower_count: int = len(profile.follows.all())
    following_count: int = len(profile.followed_by.all())
    message_count: int = Messages.objects.filter(user_id=profile.user).count()
    return render(
        request,
        "social/profile.html",
        {
            "profile": profile,
            "follower_count": follower_count,
            "following_count": following_count,
            "message_count": message_count
        },
    )