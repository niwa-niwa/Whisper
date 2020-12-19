from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('', views.UsersIndex.as_view(), name="users_index"),
    path('<int:pk>/profile/', views.UserPostsListAndCreate.as_view(), name='user_profile'),
    path('follow/<int:pk>/', views.followings, name="user_following"),
    path('unfollow/<int:pk>/', views.unfollowings, name="user_unfollowing"),
]
