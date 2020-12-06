from django.shortcuts import render
from django.views import generic

from accounts.models import CustomUser


class IndexView(generic.ListView):
    context_object_name = 'users'
    model = CustomUser
    template_name = 'users.html'
    
    def get_queryset(self):
        users = CustomUser.objects.all()
        print('result= '+ str(users))
        return users


class UserProfile(generic.DetailView):
    context_object_name = 'user'
    model = CustomUser
    template_name = 'user_profile.html'
