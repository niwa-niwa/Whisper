from django.urls import path
from . import views


app_name = 'posts'
urlpatterns = [
    path('', views.PostsIndex.as_view(), name="posts_index"),
    path('store/', views.PostStore.as_view(), name="post_store"),
    path('delete/<int:pk>/', views.delete_post, name="post_delete"),
]
