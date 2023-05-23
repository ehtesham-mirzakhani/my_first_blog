from django.shortcuts import render,HttpResponse
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html', {})
def show(request):
    return HttpResponse(request)

def post5(request):
    me = User.objects.get(Username = 'admin')
    for i in range(5):
        text = f'text{i}'
        title = f'title{i}'
        Post.objects.create(author=me ,text=text,title=title).publish()
    return HttpResponse("its done (post5)")
