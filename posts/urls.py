from django.urls import path
from . import views


app_name = 'posts'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('posts-list', views.PostsListView.as_view(), name="posts_list")
]
