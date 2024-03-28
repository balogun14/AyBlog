from multiprocessing import context
from typing import Any
from unicodedata import category
from xml.dom import NotFoundErr
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Blog

# Create your views here.


class BlogListView(ListView):
    model = Blog
    context_object_name = "blog_list"
    template_name = "home.html"


class BlogDetailView(DetailView):
    template_name = "detail.html"

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        blog = Blog.objects.filter(slug=slug)
        return blog


class CategoryListView(ListView):
    context_object_name = "blog_list"
    template_name = "category.html"

    def get_queryset(self):
        category = Blog.objects.all()
        match self.kwargs["category"]:
            case "education":
                category = category.filter(category="education")
                return category
            case "politics":
                category = category.filter(category="politics")
                return category
            case "food":
                category = category.filter(category="food")
                return category
            case "motivation":
                category = category.filter(category="motivation")
                return category
        return HttpResponse("""The requested URl does not Exist Not Found""")
