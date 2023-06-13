from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.http.response import Http404
# Create your views here.


def index(request):
    print(request)

    return HttpResponse('index')


def details(request, department_id):
    print(department_id)
    departments_map = {
        '1': "Developers",
        '2': "QA"
    }
    payload = f'Department: {departments_map.get(str(department_id), "Unknown")}'

    if department_id == 1:
        return redirect('departments template')
    # return HttpResponse(payload)
    return redirect(f'/departments/template/{department_id}', department_id=department_id)
    # return redirect('departments template')

# def details(request, *args, **kwargs):
#     print(args)
#     print(kwargs)
#     return HttpResponse('details')


def details_template(request, department_id):
    departments_map = {
        '1': "Developers",
        '2': "QA"
    }
    payload = f'Department: {departments_map.get(str(department_id), "Unknown")}'
    context = {
        "title": "Departments title from context",
        "payload": payload,
    }

    return render(request, 'departments/details.html', context=context)


def details_error(request, department_id):
    if department_id == 1:
        return HttpResponse('I have such department')
    else:
        # return HttpResponseNotFound('not found, sorry')
        return HttpResponse('not found sorry, 2', status_code=404)
    # return HttpResponse('index')
    # get_object_or_404
    # raise Http404