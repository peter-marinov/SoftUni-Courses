from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse('DB can not be displayed yet :)')


def user_info(request, user_id, user_name):
    if user_id < 10:
        user_status = 'old'
    else:
        user_status = 'new'

    context = {
        'user_id': user_id,
        'user_name': user_name,
        'user_status': user_status
    }

    return render(request, 'users/user_info.html', context=context)


def admin(request):
    return redirect('user is not admin')


def no_admin(request):
    return render(request, 'users/no_admin.html')