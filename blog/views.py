from django.shortcuts import render,HttpResponse , get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
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

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})