from django.urls import path
from . import views


app_name = 'users'
urlpatterns = [
    path('', views.UsersIndex.as_view(), name="users_index"),
    path('<int:pk>/profile/', views.UserPostsListAndCreate.as_view(), name='user_profile'),
]
