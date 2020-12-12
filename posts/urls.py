from django.urls import path
from . import views


# アプリ名を変えて作り直した方が良さそう
app_name = 'posts'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('posts/', views.PostsIndex.as_view(), name="posts_index"),
    path('store/', views.PostStore.as_view(), name="post_store"),
]
