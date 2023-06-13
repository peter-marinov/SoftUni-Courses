from django.http import HttpResponse
from django.shortcuts import render
from tasks.models import Task

# Create your views here.


def index(request):
    return HttpResponse('It works!')


def list_tasks(request):
    # all_tasks = Task.objects.all()
    all_tasks = Task.objects.order_by('id').all()
    return HttpResponse(f'{t.id} {t.title} {t.priority} \n' for t in all_tasks)


def list_tasks_template(request):
    context = {
        'title': 'My tasks for today',
        'tasks': Task.objects.order_by('id').all()
    }
    return render(request, 'tasks/tasks.html', context=context)