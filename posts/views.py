from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from .models import Post
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PostForm
from django.http import HttpResponseRedirect


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


class PostStore(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'post_store.html'
    form_class = PostForm
    # success_url = reverse_lazy('posts:posts_index')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        messages.success(self.request, 'ポストを作成しました。')
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        # return super().form_valid(form) #リダイレクトさせない場合

    def form_invalid(self, form):
        messages.error(self.request, "ポストの作成に失敗しました。")
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
        # return super().form_invalid(form)


class PostDelete(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts:posts_index')

    def delete(self, request, *args, **kwargs):
        # 自分以外の投稿は削除できないようにする
        messages.success(self.request, "投稿を削除しました。")
        return super().delete(request, *args, **kwargs)


def delete_post(request, pk):
    post = get_object_or_404(Post, id= pk)
    post.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
