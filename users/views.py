from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from accounts.models import CustomUser
from posts.models import Post


class UsersIndex(LoginRequiredMixin, generic.ListView):
    context_object_name = 'cusers'
    model = CustomUser
    template_name = 'users_index.html'
    paginate_by = 10
    
    def get_queryset(self):
        cusers = CustomUser.objects.all()
        return cusers


class UserShow(LoginRequiredMixin, generic.DetailView):
    context_object_name = 'cuser'
    model = CustomUser
    template_name = 'user_show.html'

    def get_queryset(self):
        cuser = CustomUser.objects.filter(pk=self.kwargs["pk"])
        return cuser
    


# class Posts(LoginRequiredMixin, generic.ListView):
#     context_object_name = 'post'
#     model = Post
#     template_name = 'show_posts.html'

#     def get_queryset(self):
#         print("テストです")
#         posts = Post.objects.filter(user=self.kwargs["pk"])
#         print('result= '+ str(posts) )
#         print('result= '+ str(self.kwargs["pk"]) )

