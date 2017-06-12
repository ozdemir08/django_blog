from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Post

# Create your views here.

def home(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:10]
    template = loader.get_template('blog/index.htm')
    context = {
        'latest_post_list': latest_post_list,
    }
    return HttpResponse(template.render(context, request))

def post_detail(request, url):
    post = get_object_or_404(Post, url='/'+url)
    template = loader.get_template('blog/post.htm')
    context = {
        'post': post,
    }
    return HttpResponse(template.render(context, request))
    return HttpResponse(post.content)

def reachme(request):
    return HttpResponse('Yapim asamasinda')

def about(request):
    return HttpResponse('Yapim asamasinda')

def index(request):
    return HttpResponse('Hello world!')