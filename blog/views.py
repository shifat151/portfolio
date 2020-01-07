from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
nav_status='active'
def allblogs(request):
    blogs=Blog.objects.all()
    return render(request, 'blog/allBlogs.html', {'blogs':blogs,'nav_status':nav_status})

def detail(request, blog_id):
    detailblog=get_object_or_404(Blog,pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':detailblog, 'nav_status':nav_status})