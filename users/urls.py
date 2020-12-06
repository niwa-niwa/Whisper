from django.urls import path

from . import views


app_name = 'users'
urlpatterns = [
    path('', views.IndexView.as_view(), name="users"),
    path('profile/<int:pk>/', views.UserProfile.as_view(), name='user_profile'),
]
