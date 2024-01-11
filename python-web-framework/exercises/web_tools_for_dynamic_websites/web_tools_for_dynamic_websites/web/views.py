import random
from time import sleep

from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.views.decorators import cache
from django.core.cache import cache
from django.views import generic as view

from web_tools_for_dynamic_websites.web.models import Task

UserModel = get_user_model()


# this is making cache for 2 sec for the whole view
# @cache.cache_page(2)
def index(request):
    print('In view')
    # session count how many times the page has been opened
    request.session['count'] = request.session.get('count', 0) + 1

    if not cache.get('users'):
        cache.set('users', UserModel.objects.all(), 10)

    users = cache.get('users')
    prev_tasks_ids = request.session.get('prev_tasks', [])

    context = {
        # 'count': random.randint(1, 10000),
        'count': request.session['count'],
        'users': users,
        'tasks': Task.objects.all(),
        'prev_tasks': Task.objects.filter(pk__in=prev_tasks_ids),
    }
    return render(request, 'index.html', context=context)


def details_task(request, pk):
    task = Task.objects.filter(pk=pk).get()
    prev_tasks = request.session.get('prev_tasks', [])

    prev_tasks.append(task.pk)
    start_index = max(
        0,
        len(prev_tasks) - 3,
    )
    print(request.session.get_expiry_date())
    request.session.set_expiry(5 * 60)
    request.session['prev_tasks'] = prev_tasks[start_index:]
    print(prev_tasks)

    return redirect('index')


def create_task(request):
    Task.objects.create(title=f'title {random.randint(1, 1000)}')
    return redirect('index')


class CreateTaskView(view.CreateView):
    model = Task
    template_name = 'index.html'