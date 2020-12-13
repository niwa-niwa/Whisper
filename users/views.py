from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import generic

from accounts.models import CustomUser
from posts.models import Post
from posts.forms import PostForm


class UsersIndex(LoginRequiredMixin, generic.ListView):
    context_object_name = 'cusers'
    model = CustomUser
    template_name = 'users_index.html'
    paginate_by = 10
    
    def get_queryset(self):
        cusers = CustomUser.objects.all()
        return cusers


class UserShow(LoginRequiredMixin, generic.DetailView, generic.edit.ModelFormMixin):
    context_object_name = 'cuser'
    model = CustomUser
    template_name = 'user_show.html'
    fields = ()
    # success_url = reverse_lazy('users:users_index',)

    def get_queryset(self):
        cuser = CustomUser.objects.filter(pk=self.kwargs["pk"])
        return cuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'post_form':PostForm(**self.get_form_kwargs()),
        })
        return context

    # TODO validが効いていない、returnがエラーキャッチして無理やり
    def post(self, request, *args, **kwargs):
        from django.shortcuts import redirect
        form = PostForm(**self.get_form_kwargs())

        if form.is_valid():
            query = form.save(commit=False)
            query.user = self.request.user
            # query.pk = Post.objects.get(pk=self.kwargs["pk"])
            query.save()
            print('登録が成功したはずです')
            try:
                return super().form_valid(query)
            # return self.form_valid(query)
            except:
                return redirect('users:user_profile', pk=self.request.user.pk)
        else:
            self.object = self.get_object()
            return self.form_invalid(form)
