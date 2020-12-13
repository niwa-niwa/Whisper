from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import generic

from accounts.models import CustomUser
from posts.views import PostStore


class UsersIndex(LoginRequiredMixin, generic.ListView):
    context_object_name = 'cusers'
    model = CustomUser
    template_name = 'users_index.html'
    paginate_by = 10
    
    def get_queryset(self):
        cusers = CustomUser.objects.all()
        return cusers


class UserShow(LoginRequiredMixin, generic.DetailView,):
    context_object_name = 'cuser'
    model = CustomUser
    template_name = 'user_show.html'

    def get_queryset(self):
        cuser = CustomUser.objects.filter(pk=self.kwargs["pk"])
        return cuser


class UserPostsListAndCreate(UserShow, PostStore,):
    def get(self, request, *args, **kwargs):
        form_view = PostStore.get(self, request, *args, **kwargs)
        form_view.success_url = reverse_lazy('posts:users_index')
        form_data = form_view.context_data['form']
        list_view = UserShow.get(self, request, *args, **kwargs)
        list_data = list_view.context_data['cuser']
        context = {'form':form_data, 'cuser':list_data}

        return render(request, 'user_show.html', context)
