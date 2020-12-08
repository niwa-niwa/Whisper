from django.shortcuts import render
from django.views import generic
from .models import Post

class IndexView(generic.TemplateView):
    template_name = "index.html"


class PostsListView(generic.ListView):
    model = Post
    template_name = 'posts_list.html'
    paginate_by = 20