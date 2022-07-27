from django.shortcuts import render, get_object_or_404
from main.models import Post
from django.contrib.auth.models import User

# Create your views here.
def mypage(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    posts = Post.objects.filter(writer=user)
    return render(request, 'users/mypage.html', {'posts' : posts})
