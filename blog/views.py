from django.shortcuts import render,HttpResponse , get_object_or_404,redirect
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone
from .forms import PostForms



# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'mypost': posts})
def show(request):
    return HttpResponse('request')

def post5(request):
    me = User.objects.get(username='admin')
    for i in range(5):
        text = f'text{i}'
        title = f'title{i}'
        Post.objects.create(author=me ,text=text,title=title).publish()
    return HttpResponse("its done (post5)")

def post_detail(request, pks):
    # post = Post.objects.get(pk=pks)
    post = get_object_or_404(Post, pk=pks)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pks=post.pk)
    else:
        form = PostForms()
    return render(request,'blog/post_edit.html',{'myform':form})

def post_edit(request, pks):
    post = get_object_or_404(Post, pk=pks)
    if request.method == "POST":
        form = PostForms(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pks=post.pk)
    else:
        form = PostForms(instance=post)
    return render(request, 'blog/post_edit.html', {'myform': form})