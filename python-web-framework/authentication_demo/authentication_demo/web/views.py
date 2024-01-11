from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import generic as views
# from .decorators import allow_groups

# Create your views here.
from django.contrib.auth.models import User

from authentication_demo.web.decorators import allow_groups


# Function Base Views
@login_required(login_url='/login')
def show_profile(request):
    return HttpResponse(f'You are {request.user}')


class ProfileView(auth_mixins.LoginRequiredMixin, views.View):
    # Not a good idea
    # @method_decorator(login_required())
    def get(self, request):
        return HttpResponse(f'You are {request.user}')


# @allow_groups
@allow_groups(groups=['Users statistics'])
def index(request):
    print(
        authenticate(username='peter', password='123456'),
        authenticate(username='Minkov', password='UserPass1234'),
        authenticate(username='donchominkov', password='UserPass1234')
    )
    # new_user = User.objects.create_user(
    #     username='donchominkov',
    #     password='UserPass1234',
    #     first_name='Doncho',
    #     last_name='Minkov'
    # )
    print(request.user)
    user_message = '' if request.user.is_authenticated else 'not '
    return HttpResponse(f'The user is {user_message}authenticated')


def permissions_debug(request):
    usernames = {
        'peter', # superuser
        'minkov', # user with Group
        'donchominkov',
        'Pesho'
    }
    permissions_to_check = (
        'auth.add_user',
        'auth.change_user',
        'auth.delete_user',
        'auth.view_user'
    )

    users = User.objects.filter(username__in=usernames)
    for user in users:
        print('-' * 30)
        print(f'User={user}')
        # User must have all permissions
        # print(f'Has {permissions_to_check}?')
        print(f'{permissions_to_check}: {user.has_perm(permissions_to_check)}')

        # User must have any permission
        for perm in permissions_to_check:
            print(f'{perm}: {user.has_perm(perm)}')
        print(user.user_permissions.all())
        print('-' * 30)
    return HttpResponse('It works :)')


def create_user_and_login(request):
    print(request.user)
    user = User.objects.create_user(
        username='Pesho',
        password='User.objects.create_'
    )

    # Handles the following:
    # - creates the session
    # - attaches user to request
    login(request, user)
    print(request.user)