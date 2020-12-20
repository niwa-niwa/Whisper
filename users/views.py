from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect

from accounts.models import CustomUser
from posts.views import PostStore
from users.models import UsersRelation

from django.core.exceptions import ObjectDoesNotExist


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
    slug_field = "username"
    slug_url_kwarg = "username"
    template_name = 'user_page.html'

    def get_queryset(self):
        cuser = CustomUser.objects.filter(username=self.kwargs.get("username"))
        return cuser


class UserPostsListAndCreate(UserShow, PostStore,):
    def get(self, request, *args, **kwargs):
        form_view = PostStore.get(self, request, *args, **kwargs)
        form_view.success_url = reverse_lazy('posts:users_index')
        form_data = form_view.context_data['form']
        list_view = UserShow.get(self, request, *args, **kwargs)
        list_data = list_view.context_data['cuser']
        context = {'form':form_data, 'cuser':list_data}

        return render(request, 'user_page.html', context)


class UserFollowings(PostStore):
    def get(self, request, *args, **kwargs):
        form_view = PostStore.get(self, request, *args, **kwargs)
        form_data = form_view.context_data['form']
        context = {'form':form_data}

        return render(request, 'followings.html', context)


class UserFollowers(PostStore):
    def get(self, request, *args, **kwargs):
        form_view = PostStore.get(self, request, *args, **kwargs)
        form_data = form_view.context_data['form']
        context = {'form':form_data}

        return render(request, 'followers.html', context)


# フォローする
def followings(request, username):

    user = request.user

    try:
        follow_user = get_object_or_404(CustomUser, username=username)

        UsersRelation.objects.create(following=follow_user, follower=user)

        messages.success(request, follow_user.username + 'をフォローしました。')

    except ObjectDoesNotExist:
        
        messages.error(request, '該当のユーザーは存在しません。')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# フォロー解除
def unfollowings(request, username):

    user = request.user

    try:
        follow_user = get_object_or_404(CustomUser, username=username)

        UsersRelation.objects.filter(following=follow_user, follower=user).delete()

        messages.success(request, follow_user.username + 'をフォロー解除しました。')

    except ObjectDoesNotExist:
        messages.error(request, '該当のユーザーは存在しません。')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
