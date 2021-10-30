from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def index(request):
    p = Post.objects.filter(status=1)
    allowpost = 0
    if request.user.is_authenticated:
        p = Post.objects.select_related().filter(author=request.user.id)
        allowpost = 1
    context = {
            'posts': p,
            'allowpost': allowpost,
    }
    return render(request, 'home.html', context)

def viewpost(request, post_id):

    if request.method == "POST":
        Comment.objects.create(
            post=Post.objects.get(id=int(post_id)),
            username=request.POST.get('contact-form-name'),
            email=request.POST.get('contact-form-email'),
            comment=request.POST.get('contact-form-message')
        )
    allowdelete = 0    
    if request.user.is_authenticated:
        allowdelete = 1
    context = {
            'post': Post.objects.get(id=int(post_id)),
            'comments': Comment.objects.filter(post=int(post_id)),
            'allowdelete': allowdelete,
    }
    return render(request, 'post.html', context)


def add_post(request, post_id):
    if int(post_id) == 0:
        if request.method == "POST":
            Post.objects.create(# fields = ('title','content','category','status','tags')
                author=request.user,
                title=request.POST.get('form-title'),
                content=request.POST.get('form-content'),
                category=request.POST.get('form-category'),
                status=request.POST.get('form-status'),
                tags=request.POST.get('form-tags')
            )
            return HttpResponseRedirect(reverse_lazy('blog:index'))
        else:
            context = {
                'post': "",
            }
    else:#edit
        if request.method == "POST":
            Post.objects.filter(id=post_id).update(
                title=request.POST.get('form-title'),
                content=request.POST.get('form-content'),
                category=request.POST.get('form-category'),
                status=request.POST.get('form-status'),
                tags=request.POST.get('form-tags')
            )
            return HttpResponseRedirect(reverse_lazy('blog:index'))
        else:
            context = {
                'post': Post.objects.get(id=int(post_id)),
            }
    return render(request, "addpost.html", context)

def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=int(comment_id))
    comment.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@csrf_exempt
def add_like(request, post_id):
    r=Post.objects.filter(id=post_id).update(
        likes=request.POST.get('likes')
    )
    return JsonResponse({r:r})

