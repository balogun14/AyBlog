from multiprocessing import context
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView

from .models import Blog

# Create your views here.


class BlogListView(ListView):
    model = Blog
    context_object_name = "blog_list"
    template_name = "home.html"

def detail_view(request,slug):
    detail_post = Blog.objects.filter(slug=slug)
    context = {"detail_post":detail_post}
    return render(request,"detail.html",context)