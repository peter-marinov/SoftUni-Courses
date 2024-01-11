
from django.http import HttpResponse
from django.shortcuts import render
# from django.contrib.auth.models import User

def index(request):
    # new_user = User.objects.create(
    #     username='donchominkov',
    #     password='UserPass1234',
    #     first_name='Doncho',
    #     last_name='Minkov'
    # )
    user_message = '' if request.user.is_authenticated else 'not '
    return HttpResponse(f'The user is {user_message}authenticated')

'''
Ways to create users
1. python manage.py createsuperuser
2. From admin by superuser
3. Widh code: User.object.create_user()

minkov
UserPass1234
'''