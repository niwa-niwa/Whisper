from django.shortcuts import render
from django.views import generic
from .models import Post

from django.contrib.auth.decorators import login_required

class IndexView(generic.TemplateView):
    template_name = "index.html"

class PostsListView(generic.ListView):
    context_object_name = 'posts'
    model = Post
    template_name = 'posts_list.html'
    paginate_by = 20

    def get_queryset(self):
        posts = Post.objects.filter(user=self.request.user).order_by('-created_at')
        return posts
    