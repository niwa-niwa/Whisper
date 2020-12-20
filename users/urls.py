from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('', views.UsersIndex.as_view(), name="users_index"),
    # path('home/', views.UserHome.as_views(), name='user_home')
    # path('settings/', views.UserSettings.as_views(), name='user_settings')
    path('<slug:username>/', views.UserPostsListAndCreate.as_view(), name='user_page'),
    path('<slug:username>/followings/', views.UserFollowings.as_view(), name='user_followings'),
    path('<slug:username>/followers/', views.UserFollowers.as_view(), name='user_followers'),
    path('follow/<int:pk>/', views.followings, name="user_following"),
    path('unfollow/<int:pk>/', views.unfollowings, name="user_unfollowing"),
]
