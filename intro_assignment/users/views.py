from django.shortcuts import render, get_object_or_404, redirect
from main.models import Post
from django.contrib.auth.models import User

# Create your views here.
def mypage(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    posts = Post.objects.filter(writer=user)
    return render(request, 'users/mypage.html', {'posts' : posts, 'user': user})

def follow(request, user_id):
    user = request.user
    followed_user = get_object_or_404(User, pk=user_id)
    is_follower = user.profile in followed_user.profile.followers.all()

    if is_follower:
        user.profile.followings.remove(followed_user.profile)
    else:
        user.profile.followings.add(followed_user.profile)
    return redirect('user:mypage', followed_user.id)
