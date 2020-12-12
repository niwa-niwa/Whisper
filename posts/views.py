from django.shortcuts import render
from django.views import generic
from .models import Post

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.TemplateView):
    template_name = "index.html"


class PostsIndex(LoginRequiredMixin, generic.ListView):
    context_object_name = 'posts'
    login_url = 'account_login'
    model = Post
    template_name = 'posts_index.html'
    paginate_by = 20

    def get_queryset(self):
        posts = Post.objects.filter(user=self.request.user).order_by('-created_at')
        return posts
