from django.shortcuts import render
from django.views import generic
from .models import Post

class IndexView(generic.TemplateView):
    template_name = "index.html"


class PostsListView(generic.ListView):
    model = Post
    template_name = 'posts_list.html'
    paginate_by = 20

    def get_queryset(self):
        posts = Post.objects.filter(user=self.request.user).order_by('-created_at')
        print(str(posts))
        return posts
    