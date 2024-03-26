from django.views.generic import ListView

from .models import Blog

# Create your views here.


class BlogListView(ListView):
    model = Blog
    context_object_name = "blog_list"
    template_name = "home.html"
