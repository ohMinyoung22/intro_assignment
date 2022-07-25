from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Like, Dislike
from django.utils import timezone
from django.db import models
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json
from django.contrib.auth.models import User

# Create your views here.
def showmain(request):
    posts = Post.objects.all()
    return render(request, 'main/show.html', {'posts':posts})

def showpage(request):
    return render(request, 'main/mainpage.html')

def detail(request, id):
    post = get_object_or_404(Post, pk = id)
    all_comments = post.comments.all().order_by('-created_at')
    return render(request, 'main/detail.html', {'post': post, 'comments':all_comments})

def new(request):
    return render(request, 'main/new.html')

def create(request):
    new_post = Post()
    new_post.title = request.POST['title']
    new_post.writer = request.user
    new_post.pub_date = timezone.now()
    new_post.body = request.POST['body']
    new_post.image = request.FILES.get('image')
    new_post.save()
    return redirect('main:detail', new_post.id)

def edit(request, id):
    edit_post = Post.objects.get(id = id)
    return render(request, 'main/edit.html', {'post' : edit_post})

def update(request, id):
    update_post = Post.objects.get(id = id)
    update_post.title = request.POST['title']
    update_post.writer = request.user
    update_post.pub_date = timezone.now()
    update_post.image = request.FILES.get('image')
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('main:detail', update_post.id)

def delete(request, id):
    delete_post = Post.objects.get(id = id)
    delete_post.delete()
    return redirect('main:showmain')

def create_comment(request, post_id):
    new_comment = Comment()
    new_comment.writer = request.user
    new_comment.content = request.POST['content']
    new_comment.post = get_object_or_404(Post, pk = post_id)
    new_comment.save()
    return redirect('main:detail', post_id)

def delete_comment(request,id):
    comment = get_object_or_404(Comment, pk=id)
    post_id = comment.post.id
    comment.delete()
    return redirect('main:detail', post_id)

def edit_comment(request, id):
    edit_comment = Comment.objects.get(id = id)
    return render(request, 'main/edit_comment.html', {'comment' : edit_comment})

def update_comment(request, id):
    print("update Comment content = " + request.POST['content'])
    update_comment = Comment.objects.get(id = id)
    update_comment.content = request.POST['content']
    update_comment.update_at = models.DateTimeField(auto_now=True)
    update_comment.save()
    return redirect('main:detail', update_comment.post.id)

@require_POST
@login_required
def like_toggle(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post_like, post_like_created = Like.objects.get_or_create(user = request.user, post=post)

    if not post_like_created:
        post_like.delete()
        result = "cancelled"

    else:
        result = "like"
    
    context = {
        "like_count" : post.like_count,
        "result" : result
    }

    return HttpResponse(json.dumps(context), content_type = "application/json")

def my_like(request, user_id):
    user = User.objects.get(id=user_id)
    like_list = Like.objects.filter(user = user)
    context = {
        'like_list' : like_list,
    } 

    return render(request, 'main/my_like.html', context)

@require_POST
@login_required
def dislike_toggle(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    post_dislike, post_dislike_created = Dislike.objects.get_or_create(user = request.user, post=post)

    if not post_dislike_created:
        post_dislike.delete()
        result = "cancelled"

    else:
        result = "dislike"
    
    context = {
        "dislike_count" : post.dislike_count,
        "result" : result
    }

    return HttpResponse(json.dumps(context), content_type = "application/json")

def my_dislike(request, user_id):
    user = User.objects.get(id=user_id)
    dislike_list = Dislike.objects.filter(user = user)
    context = {
        'dislike_list' : dislike_list,
    } 

    return render(request, 'main/my_dislike.html', context)

    
